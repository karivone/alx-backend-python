from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    """
    Extend this class if you want to customize how JWT authentication works,
    e.g., attach extra request.user attributes, check user status, etc.
    """
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is not None:
            user, token = user_auth_tuple
            # You can modify the user object here if needed
        return user_auth_tuple
