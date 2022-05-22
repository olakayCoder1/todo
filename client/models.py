from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TodoItem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user_id.username} --> {self.description[:10]}"



