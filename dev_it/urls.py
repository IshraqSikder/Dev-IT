"""
URL configuration for dev_it project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import HomeView, team, contact, about, course, feature, testimonial
from courses import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='home'),
    path('category/<slug:category_slug>/', course, name='category_wise_post'),
    path('users/', include('teachers.urls')),
    path('courses/', include('courses.urls')),
    path('enrollments/', include('enrollments.urls')),
    path('team/', team, name='team'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('course/', course, name='course'),
    path('feature/', feature, name='feature'),
    path('testimonial/', testimonial, name='testimonial'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)