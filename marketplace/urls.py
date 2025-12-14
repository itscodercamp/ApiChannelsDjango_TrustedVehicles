from django.urls import path
from .views import (
    VehicleListCreateView, VehicleDetailView, BannerListView,
    InquiryCreateView, MarketplaceContactCreateView
)

urlpatterns = [
    path('marketplace/vehicles', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('marketplace/vehicles/<uuid:pk>', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('marketplace/banners', BannerListView.as_view(), name='banner-list'),
    path('marketplace/inquiries', InquiryCreateView.as_view(), name='inquiry-create'),
    path('marketplace/contact', MarketplaceContactCreateView.as_view(), name='marketplace-contact'),
]
