from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('task/', views.create_and_list_task, name='create_and_list_task'),
    path('task/<int:pk>', views.modify_task, name='modify_task')
]