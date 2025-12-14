from django.urls import path
from .views import EmployeeLoginView, MarketplaceLoginView, MarketplaceRegisterView

urlpatterns = [
    path('login', EmployeeLoginView.as_view(), name='employee-login'),
    path('marketplace/auth/login', MarketplaceLoginView.as_view(), name='marketplace-login'),
    path('marketplace/auth/register', MarketplaceRegisterView.as_view(), name='marketplace-register'),
]
