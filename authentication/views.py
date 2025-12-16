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

# Keeping old views for backward compatibility if needed, or remove them.
# For this task, strict adherence to request:

