from rest_framework import generics
from .models import BonCommande
from .serializers import BonCommandeSerializer,BonCommandeListSerializer
from rest_framework.response import Response

class BonCommandeCreateView(generics.CreateAPIView):
    queryset = BonCommande.objects.all()
    serializer_class = BonCommandeSerializer
    
class AllCommandesListView(generics.ListAPIView):
    queryset = BonCommande.objects.all().order_by('-date_commande')
    serializer_class = BonCommandeListSerializer
class BonCommandeDeleteView(generics.DestroyAPIView):
    queryset = BonCommande.objects.all()
    serializer_class = BonCommandeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Categorie"))

