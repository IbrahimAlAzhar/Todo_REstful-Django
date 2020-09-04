from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self): # we add a __str__ method to provide a human-readable name for each future model instance
        return self.title
