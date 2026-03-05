import time
from collections import defaultdict
from django.http import HttpResponse


class RateLimitMiddleware:
    """Allow at most LIMIT requests per WINDOW seconds per IP for rate-limited paths."""

    LIMIT = 10
    WINDOW = 60  # seconds
    PATHS = {"/personalID/"}

    def __init__(self, get_response):
        self.get_response = get_response
        # {ip: [timestamp, ...]}
        self._requests = defaultdict(list)

    def __call__(self, request):
        if request.path in self.PATHS:
            ip = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR", ""))
            ip = ip.split(",")[0].strip()
            now = time.time()
            window_start = now - self.WINDOW
            timestamps = [t for t in self._requests[ip] if t > window_start]
            if len(timestamps) >= self.LIMIT:
                return HttpResponse("Too Many Requests", status=429)
            timestamps.append(now)
            self._requests[ip] = timestamps

        return self.get_response(request)
