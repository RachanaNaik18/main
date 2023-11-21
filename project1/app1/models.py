from django.db import models

# Create your models here.
class dj_srk(models.Model):

    name= models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.ImageField(upload_to='Images', null=True, blank=True)
    time = models.TimeField(auto_now_add=True)
    gender = models.CharField(max_length=20, default=False)
    English= models.BooleanField(default=False)
    Hindi= models.BooleanField(default=False)
    Marathi= models.BooleanField(default=False)
    city = models.CharField(max_length=100, default=False)

class Cart(models.Model):
    store = models.ForeignKey(dj_srk, on_delete=models.CASCADE)