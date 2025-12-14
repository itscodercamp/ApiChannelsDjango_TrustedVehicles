from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import MarketplaceUser
from .serializers import EmployeeLoginSerializer, MarketplaceUserLoginSerializer, MarketplaceUserSerializer
# import jwt # If using JWT

class EmployeeLoginView(APIView):
    def post(self, request):
        serializer = EmployeeLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    # Return user details or token
                    return Response({
                        "message": "Login successful",
                        "user": {
                            "id": user.id,
                            "email": user.email,
                            "username": user.username
                        }
                    }, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                pass
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarketplaceLoginView(APIView):
    def post(self, request):
        serializer = MarketplaceUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']
            try:
                user = MarketplaceUser.objects.get(phone=phone)
                if check_password(password, user.password):
                    return Response({
                        "message": "Login successful",
                        "user": MarketplaceUserSerializer(user).data
                    }, status=status.HTTP_200_OK)
            except MarketplaceUser.DoesNotExist:
                pass
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarketplaceRegisterView(APIView):
    def post(self, request):
        serializer = MarketplaceUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
