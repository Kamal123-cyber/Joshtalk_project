from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .api_views import LoginAPIView, RegisterView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),

]
