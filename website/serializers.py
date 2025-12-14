from rest_framework import serializers
from .models import ContactRequest, SellRequest, LoanRequest, InsuranceLead, PDIRequest, DealerDemoRequest

class ContactRequestSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    
    class Meta:
        model = ContactRequest
        fields = ['firstName', 'lastName', 'email', 'subject', 'message']

class SellRequestSerializer(serializers.ModelSerializer):
    regNumber = serializers.CharField(source='reg_number')
    regYear = serializers.IntegerField(source='reg_year')
    fuelType = serializers.CharField(source='fuel_type')
    kmDriven = serializers.IntegerField(source='km_driven')
    scheduledDate = serializers.DateField(source='scheduled_date')
    
    class Meta:
        model = SellRequest
        fields = [
            'make', 'model', 'variant', 'regNumber', 'regYear', 'fuelType', 
            'ownership', 'transmission', 'state', 'city', 'kmDriven', 'address', 
            'name', 'phone', 'scheduledDate'
        ]

class LoanRequestSerializer(serializers.ModelSerializer):
    loanAmount = serializers.DecimalField(source='loan_amount', max_digits=12, decimal_places=2)
    employmentType = serializers.CharField(source='employment_type')
    
    class Meta:
        model = LoanRequest
        fields = ['name', 'mobile', 'income', 'loanAmount', 'employmentType']

class InsuranceLeadSerializer(serializers.ModelSerializer):
    regNumber = serializers.CharField(source='reg_number')
    policyType = serializers.CharField(source='policy_type')
    expiryDate = serializers.DateField(source='expiry_date', required=False)
    
    class Meta:
        model = InsuranceLead
        fields = ['regNumber', 'name', 'mobile', 'policyType', 'expiryDate']

class PDIRequestSerializer(serializers.ModelSerializer):
    scheduledDate = serializers.DateField(source='scheduled_date')

    class Meta:
        model = PDIRequest
        fields = ['name', 'email', 'phone', 'city', 'make', 'model', 'scheduledDate']

class DealerDemoRequestSerializer(serializers.ModelSerializer):
    dealershipName = serializers.CharField(source='dealership_name', required=False)

    class Meta:
        model = DealerDemoRequest
        fields = ['name', 'phone', 'email', 'dealershipName']
