from django.db import models
class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100)
    def __str__(self):
        return self.nom_categorie