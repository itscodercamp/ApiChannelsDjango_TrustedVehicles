from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import MarketplaceUser
from .serializers import MarketplaceUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    # Add custom claims
    refresh['user_type'] = user.user_type
    refresh['name'] = user.full_name
    
    return str(refresh.access_token)

class AuthLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role') # Optional, for validation if needed

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # We authenticate against MarketplaceUser model
            user = MarketplaceUser.objects.get(email=email)
            if check_password(password, user.password):
                token = get_tokens_for_user(user)
                
                # Fetch related data for response
                saved_vehicles = user.favorites.values_list('vehicle_id', flat=True)
                
                return Response({
                    "token": token,
                    "user": {
                        "id": f"u_{user.id}", # Per req format
                        "name": user.full_name,
                        "email": user.email,
                        "role": user.user_type, # mapped field
                        "savedVehicles": list(saved_vehicles),
                        "savedSearches": [] # Placeholder
                    }
                }, status=status.HTTP_200_OK)
            else:
                 return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except MarketplaceUser.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class AuthRegisterView(APIView):
    def post(self, request):
        data = request.data
        # Map frontend fields to model fields if necessary
        # Frontend: name, email, password, role, dealershipName, location
        
        # Check if email exists
        if MarketplaceUser.objects.filter(email=data.get('email')).exists():
             return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_data = {
            'full_name': data.get('name'),
            'email': data.get('email'),
            'password': data.get('password'),
            'user_type': data.get('role', 'Customer').capitalize(),
            'phone': data.get('phone', '0000000000'), # Default/Unique handling might be needed
            'dealership_name': data.get('dealershipName'),
            'city': data.get('location')
        }
        
        # Phone is unique in model, so generate a dummy one if not provided (since frontend req didn't specify phone in register)
        #Ideally frontend should send phone, but we handle it.
        if 'phone' not in data:
            import random
            user_data['phone'] = str(random.randint(1000000000, 9999999999))

        serializer = MarketplaceUserSerializer(data=user_data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Registration successful",
                "user": {
                    "id": f"u_{user.id}",
                    "name": user.full_name,
                    "email": user.email,
                    "role": user.user_type
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class EmployeeLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
             return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Authenticate standard Django User (Employee/Admin)
            user = User.objects.get(email=email)
            if user.check_password(password):
                 if not user.is_active:
                     return Response({"error": "Account disabled"}, status=status.HTTP_403_FORBIDDEN)
                 
                 # Generate JWT for Employee
                 refresh = RefreshToken.for_user(user)
                 refresh['role'] = 'employee'
                 refresh['is_staff'] = user.is_staff
                 refresh['is_superuser'] = user.is_superuser
                 
                 return Response({
                    "message": "Login successful",
                    "token": str(refresh.access_token),
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "username": user.username,
                        "is_staff": user.is_staff,
                        "is_superuser": user.is_superuser
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
             return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

