from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import default_storage
from django.conf import settings
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncHour
from django.utils import timezone
from datetime import timedelta
import os
from .models import RequestLog

def index(request):
    return render(request, 'core/api_status.html')

class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        file_obj = request.FILES.get('file')
        destination = request.data.get('destination', 'uploads')
        
        if not file_obj:
            return Response({"error": "No file provided"}, status=400)
        
        # Save file
        file_path = os.path.join(destination, file_obj.name)
        saved_path = default_storage.save(file_path, file_obj)
        
        file_url = os.path.join(settings.MEDIA_URL, saved_path).replace('\\', '/')
        
        return Response({
            "success": True,
            "path": file_url
        })

class DashboardStatsView(APIView):
    def get(self, request):
        # 1. Requests per Endpoint (Top 10)
        endpoint_stats = RequestLog.objects.values('endpoint').annotate(count=Count('id')).order_by('-count')[:10]
        
        # 2. Status Code Distribution
        status_stats = RequestLog.objects.values('status_code').annotate(count=Count('id'))
        
        # 3. Requests over time (Last 24 hours, grouped by hour)
        last_24h = timezone.now() - timedelta(hours=24)
        time_stats = RequestLog.objects.filter(timestamp__gte=last_24h)\
            .annotate(time=TruncHour('timestamp'))\
            .values('time')\
            .annotate(count=Count('id'))\
            .order_by('time')
            
        return Response({
            "endpoints": list(endpoint_stats),
            "status_codes": list(status_stats),
            "timeline": list(time_stats)
        })
