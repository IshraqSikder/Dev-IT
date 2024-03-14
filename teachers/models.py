from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE, PROFESSION_TYPE

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=15, choices=GENDER_TYPE)
    profession = models.CharField(max_length=15, choices=PROFESSION_TYPE)
    image = models.ImageField(upload_to = 'teachers/media/uploads/', blank = True, null = True)
    account_no = models.IntegerField(unique=True)
    def __str__(self):
        return f"{self.user.username} - {self.account_no}"
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    city = models.CharField(max_length= 100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user.username} - {self.user.email}"
    