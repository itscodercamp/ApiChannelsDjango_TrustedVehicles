from rest_framework import serializers
from .models import Vehicle, Banner, Inquiry, MarketplaceContact

class VehicleSerializer(serializers.ModelSerializer):
    # Field Mappings (Frontend camelCase -> Backend snake_case)
    vehicleType = serializers.CharField(source='vehicle_type', required=False)
    mfgYear = serializers.IntegerField(source='mfg_year', required=False)
    regYear = serializers.IntegerField(source='reg_year', required=False)
    fuelType = serializers.CharField(source='fuel_type', required=False)
    regNumber = serializers.CharField(source='reg_number', required=False)
    rtoState = serializers.CharField(source='rto_state', required=False)
    chassisNumber = serializers.CharField(source='chassis_number', required=False)
    validUpto = serializers.DateField(source='valid_upto', required=False)
    rcAvailable = serializers.BooleanField(source='rc_available', required=False)
    insuranceExpiry = serializers.DateField(source='insurance_expiry', required=False)
    serviceHistory = serializers.CharField(source='service_history', required=False)
    odometer = serializers.IntegerField(source='km_driven', required=False)
    mainImage = serializers.ImageField(source='main_image', required=False)

    class Meta:
        model = Vehicle
        fields = '__all__'
        extra_kwargs = {
            'inspection_report': {'required': False},
            # Hide the snake_case equivalents from output if you only want camelCase, 
            # but usually keeping them or having both is okay. 
            # To be safe, we let them exist.
        }

    def to_internal_value(self, data):
        # Create a mutable copy of the data
        data = data.copy()
        
        # Initialize inspection_report if not present or parse if it is a string
        inspection_report = {}
        if 'inspection_report' in data:
            import json
            try:
                if isinstance(data['inspection_report'], str):
                    inspection_report = json.loads(data['inspection_report'])
                else:
                    inspection_report = data['inspection_report']
            except:
                pass

        # Iterate through keys to find inspection status/remarks (insp_..._status or insp_..._remark)
        keys_to_remove = []
        for key, value in data.items():
            if key.startswith('insp_') and ('_status' in key or '_remark' in key):
                # This is an inspection text field
                inspection_report[key] = value
                keys_to_remove.append(key)
        
        # Remove the flat fields from data so they don't cause "unexpected field" errors
        for key in keys_to_remove:
            del data[key]
            
        # Update/Set the inspection_report JSON
        if inspection_report:
             import json
             # Convert back to JSON string for DRF to handle it properly in form-data context
             data['inspection_report'] = json.dumps(inspection_report)

        return super().to_internal_value(data)
class BannerSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = ['title', 'image_url']
    
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'

class MarketplaceContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketplaceContact
        fields = '__all__'
