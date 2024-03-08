from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from datetime import datetime
from enrollments.models import Enrollment
from enrollments.constants import DEPOSIT
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.
def send_enrollment_email(user, subject, template):
        message = render_to_string(template, {
            'user' : user,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()
    
# class EnrollmentCreateMixin(LoginRequiredMixin, CreateView):
#     # template_name = 'transaction_form.html'
#     model = Enrollment
#     title = ''
#     success_url = reverse_lazy('enrollment_report')

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update({
#             'account': self.request.user.account
#         })
#         return kwargs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'title': self.title
#         })
#         return context
    
class EnrollmentReportView(LoginRequiredMixin, ListView):
    template_name = 'enrollment_report.html'
    model = Enrollment
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
              
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()     
            queryset = queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)
        #     self.balance = Enrollment.objects.filter(
        #         timestamp__date__gte=start_date, timestamp__date__lte=end_date).aggregate(Sum('amount'))['amount__sum']
        # else:
        #     self.balance = self.request.user.account.balance
       
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset() 
        # if queryset.exists():
        #     balance = queryset.aggregate(Sum('amount'))['amount__sum']
        # else:
        #     balance = self.request.user.account.balance
        
        context.update({
            'enrollments': queryset,
            # 'current_balance': balance
        })    
        return context