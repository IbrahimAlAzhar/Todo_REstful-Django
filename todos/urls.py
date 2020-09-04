from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path('<int:pk>',DetailTodo.as_view()), # each individual will be available at its primary key,which is a value django sets automatically in every database
    path('',ListTodo.as_view()), # list of all todos at he empty string '',in other words at api/
]
