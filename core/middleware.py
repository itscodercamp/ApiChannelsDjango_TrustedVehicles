from .models import RequestLog

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Filter out admin, static, and media requests to keep noise down
        if not any(request.path.startswith(p) for p in ['/admin/', '/static/', '/media/']):
            RequestLog.objects.create(
                endpoint=request.path,
                method=request.method,
                status_code=response.status_code
            )
            
        return response
