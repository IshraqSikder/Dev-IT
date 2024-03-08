from django.db import models
from teachers.models import UserAccount
from .constants import ENROLLMENT_TYPE
# Create your models here.


class Enrollment(models.Model):
    account = models.ForeignKey(UserAccount, related_name='enrollments', on_delete=models.CASCADE)
    # amount = models.DecimalField(decimal_places=2, max_digits=12)
    # balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12)
    enrollment_type = models.IntegerField(choices=ENROLLMENT_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
        
    def __str__(self):
        return f"{self.enrollment_type}"