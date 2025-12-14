from django.urls import path
from .views import (
    ContactRequestCreateView, SellRequestCreateView, LoanRequestCreateView,
    InsuranceLeadCreateView, PDIRequestCreateView, DealerDemoRequestCreateView,
    CarListView, CarDetailView
)

urlpatterns = [
    # 1. Sell Car
    path('sell-request', SellRequestCreateView.as_view(), name='sell-request'),
    
    # 2. Buy Car (Inventory)
    path('cars', CarListView.as_view(), name='car-list'),
    path('cars/<uuid:id>', CarDetailView.as_view(), name='car-detail'),
    
    # 3. Insurance Quote
    path('insurance/quote', InsuranceLeadCreateView.as_view(), name='insurance-quote'),
    
    # 4. Car Loan
    path('loan/apply', LoanRequestCreateView.as_view(), name='loan-apply'),
    
    # 5. PDI Booking
    path('pdi/book', PDIRequestCreateView.as_view(), name='pdi-book'),
    
    # 6. Dealer Demo
    path('dealer/demo-request', DealerDemoRequestCreateView.as_view(), name='dealer-demo'),
    
    # 7. Contact Us
    path('contact', ContactRequestCreateView.as_view(), name='contact'),
]
