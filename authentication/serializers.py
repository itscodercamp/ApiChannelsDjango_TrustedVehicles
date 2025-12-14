from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MarketplaceUser

class EmployeeLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class MarketplaceUserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

class MarketplaceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketplaceUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
