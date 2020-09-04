from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase): # here uses django's build in TestCase class
    @classmethod
    def setUpTestData(cls): # here create a dummy title and body by using setUp method
        Todo.objects.create(title='first todo',body='a body here')

    def test_title_content(self): # this method is using for check the title
        todo = Todo.objects.get(id=1) # take a object which id is 1,here we create just one object so id of this one is1
        expected_object_name = f'{todo.title}' # take the title of object which is 'first todo'
        self.assertEquals(expected_object_name,'first todo') # check both are equal or not

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name,'a body here')

