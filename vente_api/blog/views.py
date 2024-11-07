from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

from rest_framework import status
from rest_framework.response import Response

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class AllBlogsListView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-date')
    serializer_class = BlogSerializer
    
class BlogUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    partial = True
    
    
class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Blog"))
