from django.db import models
from comptes.models import CustomUser
from django.utils.timezone import now

class BonCommande(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    num_bon_commande=models.CharField(max_length=20)
    date_commande = models.DateTimeField(auto_now_add=True)
    prix_total=models.FloatField(null=True)
    
    def __str__(self):
        return self.num_bon_commande
    def save(self, *args, **kwargs):
        if not self.num_bon_commande:
            last_bon_commande = BonCommande.objects.filter(date_commande__year=now().year).last()
            if last_bon_commande:
                last_number = int(last_bon_commande.num_bon_commande.split('_')[1])
                new_number = last_number + 1
            else:
                new_number = 1
            self.num_bon_commande = f"BC_{now().year}_{new_number:04d}"
        super().save(*args, **kwargs)
