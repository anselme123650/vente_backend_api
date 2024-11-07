from rest_framework import generics
from .models import Produit
from .serializers import ProduitSerializer,ProduitListSerializer

from rest_framework import status
from rest_framework.response import Response

class ProduitListCreateView(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    
    
class ProduitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    
class AllProduitsListView(generics.ListAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitListSerializer
    
class ProduitUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    partial = True
    
    
class ProduitDeleteView(generics.DestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Produit"))
