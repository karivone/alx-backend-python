from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied
from .models import Conversation

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only participants of a conversation to interact with it.
    """

    def has_permission(self, request, view):
        # Allow only authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if the user is part of the conversation
        if request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            if hasattr(obj, 'participants'):
                return user in obj.participants.all()
            if hasattr(obj, 'conversation'):
                return user in obj.conversation.participants.all()

        return False
class IsSender(BasePermission):
    """
    Allows access only to the sender of the message.
    """

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user
