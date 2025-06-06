import logging
from datetime import datetime
from django.http import HttpResponseForbidden

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
