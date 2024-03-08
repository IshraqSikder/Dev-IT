from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from teachers.models import UserAccount
from django.contrib import messages
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

# @login_required
# def course_details(request, id):
#     course = models.Course.objects.get(id=id)
#     user = request.user
#     user_account = UserAccount.objects.filter(user=user).first()

#     if request.method == 'course':
#         form = forms.CommentForm(request.course)
#         if form.is_valid():
#             new_comment = form.save(commit=False)
#             new_comment.post = course
#             new_comment.user = user
#             new_comment.save()
#             messages.success(request, 'Comment is added successfully!')
#             return redirect('details_course', id=course.id)
#         return redirect('details_course', id=course.id)
      
#     # comments = models.Comment.objects.filter(course=course)
#     comment_form = forms.CommentForm()

#     return render(request, 'course_details.html', {'course': course, 'comment_form': comment_form})

@method_decorator(login_required, name='dispatch')
class AddCourseCreateView(CreateView):
    form_class = forms.CourseForm
    model = models.Course
    success_url = reverse_lazy('track_course')
    template_name = 'add_course.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# @login_required
# def add_course(request):
#     if request.method == 'POST':
#         course_form = forms.CourseForm(request.POST)
#         if course_form.is_valid():
#             # course_form.instance.author = request.user
#             course_form.save()
#             return redirect('track_course')
#     else: 
#         course_form = forms.CourseForm()
#     return render(request, 'add_course.html', {'form' : course_form})

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
    
class DetailCourseView(DetailView):
    model = models.Course
    pk_url_kwarg = 'id'
    template_name = 'course_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        course = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.course = course
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.object
        comments = course.comments.all()
        comment_form = forms.CommentForm()     
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context