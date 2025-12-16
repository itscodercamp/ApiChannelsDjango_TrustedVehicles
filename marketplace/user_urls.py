from django.urls import path
from .user_views import (
    UserFavoriteListCreateView, UserFavoriteDeleteView,
    UserNotificationListView, UserNotificationReadView
)

urlpatterns = [
    path('user/favorites', UserFavoriteListCreateView.as_view(), name='user-favorites'),
    path('user/favorites/<str:vehicle_id>', UserFavoriteDeleteView.as_view(), name='user-favorite-delete'),
    path('user/notifications', UserNotificationListView.as_view(), name='user-notifications'),
    path('user/notifications/<int:pk>/read', UserNotificationReadView.as_view(), name='user-notification-read'),
]
