import uuid
from django.db import models
from authentication.models import MarketplaceUser

class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    year = models.IntegerField()
    status = models.CharField(max_length=50, default='For Sale')
    
    # --- Basic Vehicle Details ---
    category = models.CharField(max_length=10, choices=(('4w', '4w'), ('2w', '2w')), default='4w')
    vehicle_type = models.CharField(max_length=20, choices=(('Private', 'Private'), ('Commercial', 'Commercial')), default='Private')
    color = models.CharField(max_length=50, blank=True, null=True)
    mfg_year = models.IntegerField(null=True, blank=True)
    reg_year = models.IntegerField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    
    variant = models.CharField(max_length=100, null=True, blank=True)
    km_driven = models.IntegerField(null=True, blank=True)
    fuel_type = models.CharField(max_length=50, null=True, blank=True)
    transmission = models.CharField(max_length=50, null=True, blank=True)
    
    reg_number = models.CharField(max_length=20, blank=True, null=True)
    chassis_number = models.CharField(max_length=50, blank=True, null=True)
    rto_state = models.CharField(max_length=50, blank=True, null=True)
    ownership = models.CharField(max_length=50, blank=True, null=True)
    valid_upto = models.DateField(null=True, blank=True)
    tax = models.CharField(max_length=50, blank=True, null=True)
    rc_available = models.BooleanField(default=False)
    scraped = models.BooleanField(default=False)
    hypothecation = models.CharField(max_length=50, blank=True, null=True)
    insurance = models.CharField(max_length=100, blank=True, null=True)
    insurance_expiry = models.DateField(null=True, blank=True)
    service_history = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    # --- Inspection Points (JSON for ~100 text fields) ---
    inspection_report = models.JSONField(default=dict, blank=True, null=True)

    # --- Files: Documents ---
    img_rc = models.ImageField(upload_to='vehicles/docs/', blank=True, null=True)
    img_noc = models.ImageField(upload_to='vehicles/docs/', blank=True, null=True)
    
    # --- Files: Gallery ---
    main_image = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    img_front = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    img_back = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    img_left = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    img_right = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    img_front_right = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_back_right = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_back_left = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_front_left = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_open_dickey = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_open_bonnet = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_roof = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_engine = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_dashboard = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_right_front_door = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_right_back_door = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    img_interior_1 = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    img_interior_2 = models.ImageField(upload_to='vehicles/', null=True, blank=True)

    # --- Files: Tyres ---
    img_tyre_1 = models.ImageField(upload_to='vehicles/tyres/', blank=True, null=True)
    img_tyre_2 = models.ImageField(upload_to='vehicles/tyres/', blank=True, null=True)
    img_tyre_3 = models.ImageField(upload_to='vehicles/tyres/', blank=True, null=True)
    img_tyre_4 = models.ImageField(upload_to='vehicles/tyres/', blank=True, null=True)
    img_tyre_optional = models.ImageField(upload_to='vehicles/tyres/', blank=True, null=True)

    # --- Files: Inspection Evidence ---
    # Structure
    img_insp_apron_1 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_apron_2 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_apron_leg_1 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_apron_leg_2 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_firewall = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_cowl_top = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    
    # Body
    img_insp_bumper = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_bonnet = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_roof = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_fender = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_door_1 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_door_2 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_door_3 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_door_4 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_pillar_1 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_pillar_2 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_pillar_3 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_pillar_4 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_pillar_5 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_pillar_6 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_quarter_panel = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_dickey_door = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)

    # Structure Extended
    img_insp_lower_cross_member = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_upper_cross_member = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)

    # Glass & Lights
    img_insp_front_show = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_windshield = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_orvm_1 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_orvm_2 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_lights_1 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_lights_2 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_fog_lights_1 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_fog_lights_2 = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    
    # Engine
    img_insp_engine_assembly = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_battery = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_engine_oil = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_engine_oil_level = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)
    img_insp_coolant = models.ImageField(upload_to='vehicles/inspection/', blank=True, null=True)

    # --- Files: Videos ---
    video_insp_engine_sound = models.FileField(upload_to='vehicles/videos/', blank=True, null=True)
    video_insp_engine_smoke = models.FileField(upload_to='vehicles/videos/', blank=True, null=True)
    video_insp_blowby = models.FileField(upload_to='vehicles/videos/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Inquiry(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(MarketplaceUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class MarketplaceContact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
