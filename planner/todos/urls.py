from django.urls import path

from . import views

urlpatterns = [
    path(r'todos/', views.TodoListView.as_view()),
    path(r'todos/<pk>', views.TodoView.as_view()),
]
