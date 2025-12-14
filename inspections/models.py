from django.db import models

class Inspection(models.Model):
    STATUS_CHOICES = (
        ('Requested', 'Requested'),
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, null=True, blank=True)
    lead_type = models.CharField(max_length=50, default='Customer') # Customer or Dealer
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Requested')
    assigned_to_id = models.CharField(max_length=50, default='Unassigned')
    
    # Optional fields
    address = models.TextField(null=True, blank=True)
    dealer_id = models.CharField(max_length=50, null=True, blank=True)
    car_year = models.CharField(max_length=4, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
