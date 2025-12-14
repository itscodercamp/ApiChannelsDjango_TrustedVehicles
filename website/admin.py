from django.contrib import admin
from .models import ContactRequest, SellRequest, LoanRequest, InsuranceLead, PDIRequest, DealerDemoRequest

# Simple registration
admin.site.register(ContactRequest)
admin.site.register(SellRequest)
admin.site.register(LoanRequest)
admin.site.register(InsuranceLead)
admin.site.register(PDIRequest)
admin.site.register(DealerDemoRequest)
