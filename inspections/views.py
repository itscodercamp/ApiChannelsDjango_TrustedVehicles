from rest_framework import generics
from .models import Inspection
from .serializers import InspectionSerializer

class InspectionListCreateView(generics.ListCreateAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

class InspectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

class WebsiteInspectionCreateView(generics.CreateAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer
    
    def perform_create(self, serializer):
        # Specific logic for website inspections if needed, e.g., setting source
        serializer.save(lead_type='Website')
