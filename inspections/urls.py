from django.urls import path
from .views import InspectionCreateView, WebsiteInspectionCreateView

urlpatterns = [
    path('inspections', InspectionCreateView.as_view(), name='create-inspection'),
    path('customerinspection', WebsiteInspectionCreateView.as_view(), name='website-inspection'),
]
