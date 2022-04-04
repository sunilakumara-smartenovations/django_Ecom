from django.db import models

# Create your models here.
class product(models.Model):
    name    = models.CharField(max_length=100)
    img     = models.ImageField(upload_to='pics')
    desc    = models.TextField()
    price   = models.IntegerField()
    offer   = models.BooleanField(default=False)
    #offer_price = models.IntegerField()
    def __str__(self):
        return str(self.name)

class contact(models.Model):
    name     = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email_ID = models.CharField(max_length=100)
    message  = models.TextField()

class slide01(models.Model):
    ttl1    = models.CharField(max_length=10)
    ttl2    = models.CharField(max_length=10)
    img     = models.ImageField(upload_to='slide01/pics')
    desc    = models.TextField()
    def __str__(self):
        return str(self.ttl1)

class slide02(models.Model):
    ttl1    = models.CharField(max_length=10)
    ttl2    = models.CharField(max_length=10)
    img     = models.ImageField(upload_to='slide02/pics')
    desc    = models.TextField()
    def __str__(self):
        return str(self.ttl2)