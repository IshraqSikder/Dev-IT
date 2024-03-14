from django.shortcuts import render
from django.template.defaultfilters import slugify
from courses.models import Course
from categories.models import Category
from teachers.models import UserAccount
from courses.models import Comment
# Create your views here.

def HomeView(request, category_slug = None):
    data = Course.objects.all()
    print(data)
    user = UserAccount.objects.all()
    comments = Comment.objects.all()
    return render(request, 'index.html', {'data' : data, 'user': user, 'comments': comments})

def team(request):
    user = UserAccount.objects.all()
    return render(request, 'team.html', {'user': user})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def course(request, category_slug = None):
    data = Course.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Course.objects.filter(category = category)
    categories = Category.objects.all()
    return render(request, 'course.html', {'data' : data, 'category' : categories})

def feature(request):
    return render(request, 'feature.html')

def testimonial(request):
    comments = Comment.objects.all()
    return render(request, 'testimonial.html', {'comments': comments})