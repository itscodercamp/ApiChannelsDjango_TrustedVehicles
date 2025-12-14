from django.urls import path
from .views import FileUploadView, DashboardStatsView

urlpatterns = [
    path('upload', FileUploadView.as_view(), name='file-upload'),
    path('stats', DashboardStatsView.as_view(), name='dashboard-stats'),
]
