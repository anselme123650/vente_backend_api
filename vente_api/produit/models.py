from django.db import models
from categorie.models import Categorie

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class Produit(models.Model):
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE)
    nom_produit = models.CharField(
        max_length=100, blank=False, null=False)
    description = models.TextField()
    qte_stock = models.IntegerField()
    prix = models.FloatField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
