from django.contrib import admin

from .models import Vehicle, Banner, Inquiry, MarketplaceContact

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'variant', 'price', 'status', 'created_at')
    search_fields = ('make', 'model', 'variant', 'reg_number')
    list_filter = ('status', 'vehicle_type', 'fuel_type')

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Banner)
admin.site.register(Inquiry)
admin.site.register(MarketplaceContact)
