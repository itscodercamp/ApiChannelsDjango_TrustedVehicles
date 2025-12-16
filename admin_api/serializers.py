from rest_framework import serializers

# Import existing serializers to reuse logic (especially Vehicle logic)
from authentication.serializers import MarketplaceUserSerializer
from marketplace.serializers import (
    VehicleSerializer, BannerSerializer, InquirySerializer, 
    MarketplaceContactSerializer, FavoriteSerializer, NotificationSerializer
)
from inspections.serializers import InspectionSerializer
from website.serializers import (
    ContactRequestSerializer, SellRequestSerializer, LoanRequestSerializer,
    InsuranceLeadSerializer, PDIRequestSerializer, DealerDemoRequestSerializer
)

# If any admin-specific modifications are needed, we can subclass here.
# For now, straightforward re-export or usage is sufficient.
