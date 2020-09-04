# we need to transform our data,from the models,into JSON that will be outputted at the URLS,so we need a serializer
# django rest framework ships with a powerful build in serializers class that we can quickly extend with a small code
from rest_framework import serializers
from .models import Todo


class TodoSerialzier(serializers.ModelSerializer): # this is serializer which is like to model in traditional django,it converts Model into JSON format
    class Meta:
        model = Todo
        fields = ('id','title','body') # id is build in from django so we didn't have to define it in our model but we will use it in our detail view
