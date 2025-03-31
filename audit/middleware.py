from .models import RequestLog


class RequestLoggingMiddleware:
    """Middleware to log incoming HTTP requests."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get info before view
        response = self.get_response(request)

        # Avoid logging static files and admin paths
        if request.path.startswith("/static/") or request.path.startswith("/favicon"):
            return response

        # Get user info
        username = request.user.username if request.user.is_authenticated else None

        # Save log
        RequestLog.objects.create(
            method=request.method,
            path=request.path,
            query_string=request.META.get("QUERY_STRING", ""),
            remote_ip=request.META.get("REMOTE_ADDR"),
            user=username,
        )

        return response
