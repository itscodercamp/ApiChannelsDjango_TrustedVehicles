from rest_framework import generics, permissions, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vehicle, Banner, Inquiry, MarketplaceContact, Favorite, Notification
from .serializers import (
    VehicleSerializer, BannerSerializer, InquirySerializer, MarketplaceContactSerializer,
    FavoriteSerializer, NotificationSerializer
)

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    # Filter Config
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'status': ['exact'],
        'make': ['exact', 'icontains'],
        'model': ['exact', 'icontains'],
        'price': ['gte', 'lte'], # min_price, max_price
        'year': ['gte'], # min_year
        'fuel_type': ['exact'],
        'transmission': ['exact'],
        'rto_state': ['exact', 'icontains'], # city/state approximation
        'vehicle_type': ['exact'],
        'category': ['exact']
    }
    search_fields = ['make', 'model', 'variant']
    ordering_fields = ['price', 'year', 'created_at']

class VehicleDetailView(generics.RetrieveUpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    parser_classes = (MultiPartParser, FormParser)

class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer

class InquiryCreateView(generics.CreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [permissions.IsAuthenticated] # Require auth

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MarketplaceContactCreateView(generics.CreateAPIView):
    queryset = MarketplaceContact.objects.all()
    serializer_class = MarketplaceContactSerializer
