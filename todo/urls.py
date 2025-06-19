from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_create, name='todo_list_create'),
    path('delete/<int:todo_id>', views.delete_todo, name = 'delete_todo'),
    path('complete<int:todo_id>', views.complete_todo, name = 'complete_todo')
]
