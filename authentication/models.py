from django.db import models

# Create your models here.
class Profile(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    psw = models.CharField(max_length=50)
    _date = models.DateField(auto_now_add=True)