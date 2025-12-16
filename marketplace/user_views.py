from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Favorite, Notification
from .serializers import FavoriteSerializer, NotificationSerializer, VehicleSerializer

class UserFavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        # Specific response format requested: Array of full Vehicle objects
        queryset = self.get_queryset()
        # Extract vehicle objects from favorites
        vehicles = [fav.vehicle for fav in queryset]
        serializer = VehicleSerializer(vehicles, many=True, context={'request': request})
        return Response(serializer.data)

class UserFavoriteDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, vehicle_id):
        try:
            favorite = Favorite.objects.get(user=request.user, vehicle__id=vehicle_id)
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
             return Response({"error": "Not found in favorites"}, status=status.HTTP_404_NOT_FOUND)

class UserNotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

class UserNotificationReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            notification = Notification.objects.get(pk=pk, user=request.user)
            notification.is_read = True
            notification.save()
            return Response({"status": "Marked as read"}, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
             return Response({"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)
