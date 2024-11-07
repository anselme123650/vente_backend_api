from django.urls import path
from .views import ProduitListCreateView, ProduitDeleteView,AllProduitsListView,ProduitDetailView,ProduitUpdateView

urlpatterns = [
    path('', ProduitListCreateView.as_view(), name='movie-list-create'),
    path('<int:pk>/', ProduitDetailView.as_view(), name='movie-detail'),
    path('all/', AllProduitsListView.as_view(), name='all-movies-list'),  
    path('delete/<int:pk>/', ProduitDeleteView.as_view(), name='movie-delete'), 
    path('update/<int:pk>/', ProduitUpdateView.as_view(), name='movie-update'), 
]