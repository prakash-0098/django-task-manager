from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('task/', views.createTaskAndList, name="create_task_list"),
    path('task/<int:pk>', views.modifyTask, name="modify_task")
]