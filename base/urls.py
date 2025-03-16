from django.urls import path
from .views import todoList, viewTask, addTask, updateTask, deleteTask, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(next_page = "login"), name = "logout"),
    path('register/', RegisterPage.as_view(), name = "register"),
    path('',todoList.as_view(),name = "todoList"),
    path('task/<int:pk>',viewTask.as_view(), name = "viewTask"),
    path('addTask', addTask.as_view(), name = "addTask"),
    path('update-task/<int:pk>', updateTask.as_view(), name = "updateTask"),
    path('delete-task/<int:pk>', deleteTask.as_view(), name = "deleteTask")
]