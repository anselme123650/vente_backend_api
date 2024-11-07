from rest_framework import generics
from .models import Categorie
from .serializers import CategorieSerializer

from rest_framework import status
from rest_framework.response import Response

class CategorieListCreateView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
    
class CategorieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
class AllCategoriesListView(generics.ListAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
class CategorieUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    partial = True
    
    
class CategorieDeleteView(generics.DestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Categorie"))
