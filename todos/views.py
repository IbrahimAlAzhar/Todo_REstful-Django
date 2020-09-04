from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerialzier  # import TodoSerializer from serializers.py file

# here we are just building an API,therefore we do not need to create any template files or traditional django views
# instead we will update three files that are django REST framework specific to transform our database model into a web api:urls.py,views.py and serializers.py
# in traditional django views are used to customize what data to send to the templates,in django rest framework views do the same thing but for our serialized data,here ships with generic views for common use cases


# here we use ListAPIView to display all todos and RetriveAPIView to display a single model instance
class ListTodo(generics.ListAPIView):  # inherits from generic List view
    queryset = Todo.objects.all()
    serializer_class = TodoSerialzier


class DetailTodo(generics.RetrieveAPIView):  # RetriveAPIView is like as detailview in traditional django
    queryset = Todo.objects.all()
    serializer_class = TodoSerialzier

# the difference between django REST framework and django is that django rest framework we need to add a serializers.py
# file and we don not need a template file otherwise the urls.py file and views.py files act in a similar manner.

