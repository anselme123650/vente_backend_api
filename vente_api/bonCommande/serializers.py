from rest_framework import serializers
from .models import BonCommande
from commande.models import Commande
from commande.serializers import CommandeSerializer
from comptes.serializers import RegisterSerializer
class BonCommandeSerializer(serializers.ModelSerializer):
    commandes = CommandeSerializer(many=True)
    class Meta:
        model = BonCommande
        fields = ['id', 'user','num_bon_commande','prix_total', 'date_commande', 'commandes']
        read_only_fields = ['num_bon_commande']

    def create(self, validated_data):
        commandes_data = validated_data.pop('commandes')
        bon_commande = BonCommande.objects.create(**validated_data)
        for commande_data in commandes_data:
            Commande.objects.create(bon=bon_commande, **commande_data)
        return bon_commande
class BonCommandeListSerializer(serializers.ModelSerializer):
    user=RegisterSerializer()
    commandes = CommandeSerializer(many=True)
    class Meta:
        model = BonCommande
        fields = ['id', 'user','num_bon_commande','prix_total', 'date_commande', 'commandes']
