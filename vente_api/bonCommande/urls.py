from django.urls import path
from .views import BonCommandeCreateView,AllCommandesListView,BonCommandeDeleteView

urlpatterns = [
    path('', BonCommandeCreateView.as_view(), name='command-list-create'),
    path('all/', AllCommandesListView.as_view(), name='commande-all-list'),
    path('delete/<int:pk>/', BonCommandeDeleteView.as_view(), name='commande-delete'),
]