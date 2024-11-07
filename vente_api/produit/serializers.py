from rest_framework import serializers
from .models import Produit
from categorie.serializers import CategorieSerializer

class ProduitListSerializer(serializers.ModelSerializer):
    categorie=CategorieSerializer()
    class Meta:
        model = Produit
        fields = ['id','nom_produit','description','qte_stock','prix','image_url','categorie']

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'