from django.urls import path
from .views import CategorieListCreateView, CategorieDetailView,AllCategoriesListView,CategorieDeleteView,CategorieUpdateView

urlpatterns = [
    path('', CategorieListCreateView.as_view(), name='movie-list-create'),
    path('<int:pk>/', CategorieDetailView.as_view(), name='movie-detail'),
    path('all/', AllCategoriesListView.as_view(), name='all-movies-list'),  
    path('delete/<int:pk>/', CategorieDeleteView.as_view(), name='movie-delete'), 
    path('update/<int:pk>/', CategorieUpdateView.as_view(), name='movie-update'), 
]