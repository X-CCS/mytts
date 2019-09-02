# Create your models here.
from django.conf import settings
from django.db import models
from django.db import models


class Transcript(models.Model):
    transcript = models.TextField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
