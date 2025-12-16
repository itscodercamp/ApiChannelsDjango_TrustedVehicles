from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, VehicleViewSet, InquiryViewSet, BannerViewSet, MarketplaceContactViewSet,
    FavoriteViewSet, NotificationViewSet, InspectionViewSet, WebsiteContactViewSet,
    SellRequestViewSet, LoanRequestViewSet, InsuranceLeadViewSet, PDIRequestViewSet,
    DealerDemoRequestViewSet
)

router = DefaultRouter()

# Auth
router.register(r'users', UserViewSet)

# Marketplace
router.register(r'marketplace/vehicles', VehicleViewSet)
router.register(r'marketplace/inquiries', InquiryViewSet)
router.register(r'marketplace/banners', BannerViewSet)
router.register(r'marketplace/contacts', MarketplaceContactViewSet)
router.register(r'marketplace/favorites', FavoriteViewSet)
router.register(r'marketplace/notifications', NotificationViewSet)

# Inspection
router.register(r'inspections', InspectionViewSet)

# Website
router.register(r'website/contacts', WebsiteContactViewSet)
router.register(r'website/sell-requests', SellRequestViewSet)
router.register(r'website/loan-requests', LoanRequestViewSet)
router.register(r'website/insurance-leads', InsuranceLeadViewSet)
router.register(r'website/pdi-requests', PDIRequestViewSet)
router.register(r'website/dealer-demos', DealerDemoRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
