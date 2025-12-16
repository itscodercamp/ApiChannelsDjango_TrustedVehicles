from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

# Models
from authentication.models import MarketplaceUser
from marketplace.models import (
    Vehicle, Banner, Inquiry, MarketplaceContact, Favorite, Notification
)
from inspections.models import Inspection
from website.models import (
    ContactRequest, SellRequest, LoanRequest, InsuranceLead, 
    PDIRequest, DealerDemoRequest
)

# Serializers
from .serializers import (
    MarketplaceUserSerializer, VehicleSerializer, BannerSerializer, 
    InquirySerializer, MarketplaceContactSerializer, FavoriteSerializer, 
    NotificationSerializer, InspectionSerializer, ContactRequestSerializer, 
    SellRequestSerializer, LoanRequestSerializer, InsuranceLeadSerializer, 
    PDIRequestSerializer, DealerDemoRequestSerializer
)

class BaseAdminViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    pagination_class = None # Admin panels often prefer full lists or custom paging; keeping default or None.
                            # Actually, default paging from settings is safer for large datasets.
                            # If pagination_class is custom defined in settings as PageNumberPagination, it applies.

# --- Authentication ---
class UserViewSet(BaseAdminViewSet):
    queryset = MarketplaceUser.objects.all()
    serializer_class = MarketplaceUserSerializer
    search_fields = ['full_name', 'email', 'phone', 'dealership_name']
    filterset_fields = ['user_type', 'city']

# --- Marketplace ---
class VehicleViewSet(BaseAdminViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    search_fields = ['make', 'model', 'variant', 'reg_number', 'id'] # ID string search
    filterset_fields = ['status', 'category', 'vehicle_type', 'fuel_type', 'transmission']

class InquiryViewSet(BaseAdminViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    search_fields = ['message', 'user__full_name', 'user__email', 'vehicle__make']
    filterset_fields = ['vehicle', 'user']

class BannerViewSet(BaseAdminViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    filterset_fields = ['is_active']

class MarketplaceContactViewSet(BaseAdminViewSet):
    queryset = MarketplaceContact.objects.all()
    serializer_class = MarketplaceContactSerializer
    search_fields = ['name', 'email', 'message']

class FavoriteViewSet(BaseAdminViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    filterset_fields = ['user', 'vehicle']

class NotificationViewSet(BaseAdminViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    search_fields = ['title', 'message']
    filterset_fields = ['user', 'type', 'is_read']

# --- Inspections ---
class InspectionViewSet(BaseAdminViewSet):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer
   # search_fields might need adjustment based on Inspection model fields

# --- Website Requests ---
class WebsiteContactViewSet(BaseAdminViewSet):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer
    search_fields = ['first_name', 'last_name', 'email', 'subject']

class SellRequestViewSet(BaseAdminViewSet):
    queryset = SellRequest.objects.all()
    serializer_class = SellRequestSerializer
    search_fields = ['name', 'phone', 'make', 'model']

class LoanRequestViewSet(BaseAdminViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    search_fields = ['name', 'mobile', 'employment_type']

class InsuranceLeadViewSet(BaseAdminViewSet):
    queryset = InsuranceLead.objects.all()
    serializer_class = InsuranceLeadSerializer
    search_fields = ['name', 'mobile', 'reg_number']

class PDIRequestViewSet(BaseAdminViewSet):
    queryset = PDIRequest.objects.all()
    serializer_class = PDIRequestSerializer
    search_fields = ['name', 'phone', 'make']

class DealerDemoRequestViewSet(BaseAdminViewSet):
    queryset = DealerDemoRequest.objects.all()
    serializer_class = DealerDemoRequestSerializer
    search_fields = ['name', 'phone', 'dealership_name']
