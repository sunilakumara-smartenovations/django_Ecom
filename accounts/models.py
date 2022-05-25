from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    phone_no = models.CharField(max_length=12)
    otp = models.CharField(max_length=20,null=True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4)