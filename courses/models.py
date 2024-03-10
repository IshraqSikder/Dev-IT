from django.db import models
from categories.models import Category
from teachers.models import UserAccount
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    category = models.ManyToManyField(Category) 
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'courses/media/uploads/', blank = True, null = True)
    borrowers = models.ManyToManyField(User, related_name='borrowed_course', blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'Commented by {self.name}'