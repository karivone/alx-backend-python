from rest_framework import permissions

class IsParticipant(permissions.BasePermission):
    """
    Allows access only to users who are participants in the conversation.
    """

    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()


class IsSender(permissions.BasePermission):
    """
    Allows access only to the sender of the message.
    """

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user
