from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from teachers.models import UserAccount
from django.contrib import messages
from enrollments.models import Enrollment
from enrollments.constants import ENROLL, COMPLETE
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# Create your views here.
def confirmation_email(user, subject, template):
        message = render_to_string(template, {
            'user' : user,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

@login_required
def course_details(request, id):
    course = models.Course.objects.get(id=id)
    user = request.user
    user_account = UserAccount.objects.filter(user=user).first()
    borrowers_list = []
    return_list = []

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.course = course
            new_comment.user = user
            new_comment.save()
            messages.success(request, 'Comment is added successfully!')
            return redirect('details_course', id=course.id)
        
        if 'borrow' in request.POST:
            Enrollment.objects.create(
                account=user_account,
                enrollment_type=ENROLL
            )
            course.borrowers.add(user)
            borrowers_list.append(course)
            print(borrowers_list)
            messages.success(request, 'Course is enrolled successfully!')
            confirmation_email(user, 'Enroll Course Message','enroll_email.html')
            
        elif 'return' in request.POST:
            Enrollment.objects.create(
                account=user_account,
                enrollment_type=COMPLETE
            )
            course.borrowers.remove(user)
            return_list.append(user)
            messages.success(request, 'Course is completed successfully!')
            confirmation_email(user, 'Complete Course Message','complete_email.html')

        return redirect('details_course', id=course.id)
      
    comments = models.Comment.objects.filter(course=course)
    comment_form = forms.CommentForm()

    return render(request, 'course_details.html', {'course': course, 'comments': comments, 'comment_form': comment_form})

@method_decorator(login_required, name='dispatch')
class AddCourseCreateView(CreateView):
    form_class = forms.CourseForm
    model = models.Course
    success_url = reverse_lazy('track_course')
    template_name = 'add_course.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')  
class EditCourseView(UpdateView):
    form_class = forms.CourseForm
    model = models.Course
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('track_course')
    template_name = 'add_course.html'
    
@method_decorator(login_required, name='dispatch')
class DeleteCourseView(DeleteView):
    model = models.Course
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('track_course')
    template_name = 'delete.html'
    