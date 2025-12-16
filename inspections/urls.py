from django.urls import path
from .views import InspectionListCreateView, InspectionDetailView, WebsiteInspectionCreateView

urlpatterns = [
    path('inspections', InspectionListCreateView.as_view(), name='inspection-list-create'),
    path('inspections/<int:pk>', InspectionDetailView.as_view(), name='inspection-detail'),
    path('customerinspection', WebsiteInspectionCreateView.as_view(), name='website-inspection'),
]
