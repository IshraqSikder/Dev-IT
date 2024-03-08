from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.AddCourseCreateView.as_view(), name = 'add_course'),
    path('edit/<int:id>', views.EditCourseView.as_view(), name = 'edit_course'),
    path('delete/<int:id>', views.DeleteCourseView.as_view(), name = 'delete_course'),
    path('details/<int:id>', views.DetailCourseView.as_view(), name = 'details_course'),
]