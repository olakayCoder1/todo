from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AccountActivation(models.Model):
    active_token = models.CharField(max_length=110)






class Profile(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    user_image = models.ImageField(upload_to="media", default="astro-a40.jpg")
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='None')
    join_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.user_id.username} profile"







