from django.urls import path
from . import views



from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    #Authentication
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/register/', views.RegisterAdminView.as_view(), name='auth_admin_register'),
    path('register/', views.RegisterView.as_view(), name='auth_admin_register'),
    path('', views.getRoutes),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('list/', views.UserListView.as_view(), name='users-list'),
     path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='users-delete'),

]