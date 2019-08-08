from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Survey(models.Model):
    coordinator = models.CharField(max_length=100)
    student = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    question = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_complete = models.BooleanField(default=True)
    owner= models.ForeignKey(User, related_name="surveys", on_delete=models.CASCADE, null=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.coordinator