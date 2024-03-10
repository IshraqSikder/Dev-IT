from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from datetime import datetime
from enrollments.models import Enrollment
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
       
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset() 
        
        context.update({
            'enrollments': queryset,
        })  
        return context