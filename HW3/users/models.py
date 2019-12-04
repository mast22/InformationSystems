from django.db import models as m
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    status = m.CharField(max_length=100)

    def __str__(self):
        return self.username
