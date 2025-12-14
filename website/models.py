from django.db import models

class ContactRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SellRequest(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=20)
    reg_year = models.IntegerField()
    fuel_type = models.CharField(max_length=50)  # Petrol, Diesel, CNG, EV, etc.
    ownership = models.CharField(max_length=50)  # 1st, 2nd, etc.
    transmission = models.CharField(max_length=50) # Manual, Automatic
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    km_driven = models.IntegerField()
    address = models.TextField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    scheduled_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class LoanRequest(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    income = models.DecimalField(max_digits=12, decimal_places=2)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    employment_type = models.CharField(max_length=50) # salaried, self
    created_at = models.DateTimeField(auto_now_add=True)

class InsuranceLead(models.Model):
    reg_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    policy_type = models.CharField(max_length=50) # comprehensive, third-party, etc.
    expiry_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PDIRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    scheduled_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class DealerDemoRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    dealership_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
