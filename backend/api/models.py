from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    # We define python version of this model
    # then Django will convert it to SQL (ORM!!!!!)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Each user will have a specific list of notes
    # if user deleted, delete all notes = cascade
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title