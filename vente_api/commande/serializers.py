from rest_framework import serializers
from .models import Commande
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ['id', 'produit', 'qte']
    def create(self, validated_data):
        return super().create(validated_data)