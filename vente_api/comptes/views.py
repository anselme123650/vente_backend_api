from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from comptes.serializers import MyTokenObtainPairSerializer, RegisterAdminSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import  CustomUser
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
import json


# Create your views here.

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterAdminView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterAdminSerializer
    
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # Si 'client' est présent, il doit être un dictionnaire ou une chaîne JSON
        if 'client' in request.data:
            # Si le champ client est déjà un dictionnaire, on le laisse tel quel
            if isinstance(request.data['client'], str):
                try:
                    # Si le champ client est une chaîne JSON, le décoder
                    client_data = json.loads(request.data['client'])
                    request.data['client'] = client_data
                except json.JSONDecodeError:
                    return Response({"error": "Invalid JSON in client field"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                print("Le champ 'client' est déjà un dictionnaire:", request.data['client'])
                
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return super().create(request, *args, **kwargs)
        else:
            # Afficher les erreurs de validation
            print("Erreur de validation:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/prediction/'
    ]
    return Response(routes)
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='User')
    serializer_class = RegisterSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username', 'email'] 
    ordering = ['username']
    def get_queryset(self):
        return self.queryset
class UserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Categorie"))

