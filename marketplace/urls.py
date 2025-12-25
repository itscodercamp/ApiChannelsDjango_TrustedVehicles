from django.urls import path
from .views import (
    VehicleListCreateView, VehicleDetailView, BannerListView,
    InquiryCreateView, MarketplaceContactCreateView
)

urlpatterns = [
    path('marketplace/vehicles/', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('marketplace/vehicles/<str:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('marketplace/banners/', BannerListView.as_view(), name='banner-list'),
    path('marketplace/inquiries/', InquiryCreateView.as_view(), name='inquiry-create'),
    path('marketplace/contact/', MarketplaceContactCreateView.as_view(), name='marketplace-contact'),
]

# Include user feature URLs (namespaced or flat)
from .user_urls import urlpatterns as user_urlpatterns
urlpatterns += user_urlpatterns
