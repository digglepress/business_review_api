from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    description = models.TextField()
