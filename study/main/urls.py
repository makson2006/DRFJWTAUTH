from django.urls import path
from .views import MenAPIView,MenRUDAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('api/v1/men/', MenAPIView.as_view(), name='men-list-create'),
    path('api/v1/men/<int:pk>/', MenRUDAPIView.as_view(), name='men-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
]
