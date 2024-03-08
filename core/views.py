from django.shortcuts import render
from django.template.defaultfilters import slugify
from courses.models import Course
from categories.models import Category
# Create your views here.

def HomeView(request, category_slug = None):
    data = Course.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Course.objects.filter(category = category)
    categories = Category.objects.all()
    return render(request, 'index.html', {'data' : data, 'category' : categories})