from django.urls import path
from .views import AuthLoginView, AuthRegisterView

urlpatterns = [
    path('auth/login', AuthLoginView.as_view(), name='auth-login'),
    path('auth/register', AuthRegisterView.as_view(), name='auth-register'),
]
