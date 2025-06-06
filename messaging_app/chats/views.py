from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from django.shortcuts import render

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__username']

    # POST /conversations/ to create a new conversation (already handled by ModelViewSet create)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['message_body']

    def create(self, request, *args, **kwargs):
        # Override create to ensure message is linked to a conversation
        conversation_id = request.data.get('conversation')
        if not conversation_id:
            return Response({"error": "Conversation ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

# Create your views here.
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)
