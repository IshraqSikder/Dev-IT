from django.urls import path
from .views import UserRegistrationView, UserLoginView ,UserAccountUpdateView
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', UserAccountUpdateView.as_view(), name='profile' ),
    path('track_course/', views.track_course, name='track_course' ),
    path('change_password/', views.pass_change, name='change_password'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
]