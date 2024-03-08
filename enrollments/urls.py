from django.urls import path
from .views import EnrollmentReportView

urlpatterns = [
    path("report/", EnrollmentReportView.as_view(), name="enrollment_report"),
]