from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Scores(models.Model):
    result = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

