import logging
from datetime import datetime
from django.http import HttpResponseForbidden
from collections import defaultdict

# Configure logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler('requests.log')
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_entry = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logger.info(log_entry)

        response = self.get_response(request)
        return response
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current hour in 24-hour format
        current_hour = datetime.now().hour

        # Block access outside 6PM to 9PM (i.e., before 18 or after 21)
        if current_hour < 18 or current_hour >= 21:
            return HttpResponseForbidden("Access to chat is restricted at this time. Try between 6PM and 9PM.")

        # Proceed to the view
        response = self.get_response(request)
        return response
class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Track IP -> [timestamps]
        self.message_history = defaultdict(list)
        self.TIME_WINDOW = 60  # seconds
        self.MAX_MESSAGES = 5

    def __call__(self, request):
        if request.method == 'POST' and '/messages/' in request.path:
            ip_address = self.get_client_ip(request)
            current_time = time.time()

            # Remove messages older than TIME_WINDOW
            self.message_history[ip_address] = [
                ts for ts in self.message_history[ip_address]
                if current_time - ts < self.TIME_WINDOW
            ]

            if len(self.message_history[ip_address]) >= self.MAX_MESSAGES:
                return HttpResponseForbidden("Rate limit exceeded: Max 5 messages per minute.")

            self.message_history[ip_address].append(current_time)

        return self.get_response(request)

    def get_client_ip(self, request):
        """Get IP from request (handle proxies if any)."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip checks for admin login or static/media paths
        if request.path.startswith('/admin/') or request.path.startswith('/static/'):
            return self.get_response(request)

        # Skip unauthenticated users
        if not request.user.is_authenticated:
            return self.get_response(request)

        # Check user role (assuming `role` is a field on the User model or profile)
        user = request.user
        user_role = getattr(user, 'role', None)  # or use user.profile.role if stored in profile

        allowed_roles = ['admin', 'moderator']
        if user_role not in allowed_roles:
            return HttpResponseForbidden("Access denied: You do not have the required role.")

        return self.get_response(request)
