from django.urls import path
from .views import BlogListCreateView, BlogDetailView,AllBlogsListView,BlogDeleteView,BlogUpdateView

urlpatterns = [
    path('', BlogListCreateView.as_view(), name='blog-list-create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('all/', AllBlogsListView.as_view(), name='all-blogs-list'),  
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'), 
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'), 
]