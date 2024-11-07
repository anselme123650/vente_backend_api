from django.db import models
from bonCommande.models import BonCommande
from produit.models import Produit

class Commande(models.Model):
    bon=models.ForeignKey(BonCommande,related_name='commandes', on_delete=models.CASCADE)
    produit=models.ForeignKey(Produit, on_delete=models.CASCADE)
    qte = models.IntegerField()
    
    def __str__(self):
        return self.id