from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from marketplace.models import Vehicle
from marketplace.serializers import VehicleSerializer
from .models import (
    ContactRequest, SellRequest, LoanRequest, InsuranceLead, PDIRequest, DealerDemoRequest
)
from .serializers import (
    ContactRequestSerializer, SellRequestSerializer, LoanRequestSerializer,
    InsuranceLeadSerializer, PDIRequestSerializer, DealerDemoRequestSerializer
)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100

class CarListView(generics.ListAPIView):
    serializer_class = VehicleSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        queryset = Vehicle.objects.filter(status='For Sale')
        
        # Search (Make or Model)
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(Q(make__icontains=search) | Q(model__icontains=search))
            
        # Fuel Type
        fuel_type = self.request.query_params.get('fuelType', None)
        if fuel_type and fuel_type != 'All':
            queryset = queryset.filter(fuel_type__iexact=fuel_type)
            
        # Price Range
        min_price = self.request.query_params.get('minPrice', None)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
            
        max_price = self.request.query_params.get('maxPrice', None)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
            
        return queryset

class CarDetailView(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = 'id'

class ContactRequestCreateView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

class SupportContactView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

class SellRequestCreateView(generics.CreateAPIView):
    queryset = SellRequest.objects.all()
    serializer_class = SellRequestSerializer

class LoanRequestCreateView(generics.CreateAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer

class InsuranceLeadCreateView(generics.CreateAPIView):
    queryset = InsuranceLead.objects.all()
    serializer_class = InsuranceLeadSerializer

class PDIRequestCreateView(generics.CreateAPIView):
    queryset = PDIRequest.objects.all()
    serializer_class = PDIRequestSerializer

class DealerDemoRequestCreateView(generics.CreateAPIView):
    queryset = DealerDemoRequest.objects.all()
    serializer_class = DealerDemoRequestSerializer
