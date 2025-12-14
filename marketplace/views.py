from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Vehicle, Banner, Inquiry, MarketplaceContact
from .serializers import VehicleSerializer, BannerSerializer, InquirySerializer, MarketplaceContactSerializer

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def get_queryset(self):
        # Allow filtering by status if provided, else return all
        queryset = Vehicle.objects.all()
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status=status_param)
        return queryset

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

class MarketplaceContactCreateView(generics.CreateAPIView):
    queryset = MarketplaceContact.objects.all()
    serializer_class = MarketplaceContactSerializer
