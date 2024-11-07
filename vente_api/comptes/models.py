from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nom_client = models.CharField(max_length=100,null=True)
    adresse= models.CharField(max_length=150,null=True)
    telephone=models.CharField(max_length=30,null=True)
    role = models.CharField(max_length=255, blank=True)
    photo_url = models.ImageField(upload_to='covers/', null=True, blank=True)
    

    def __str__(self):
        return self.username
