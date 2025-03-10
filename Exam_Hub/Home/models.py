from django.db import models

# Create your models here.


class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.username

