from django.db import models

# Create your models here.

class contact(models.Model):
    name     = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email_ID = models.CharField(max_length=100)
    message  = models.TextField()
    def __str__(self) :
        return str(self.name)