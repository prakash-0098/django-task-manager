from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('task/', views.createTask, name="create_task"),
    path('task/<int:pk>', views.taskDetails, name="get_update_delete")
]