from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    # POST /conversations/ to create a new conversation (already handled by ModelViewSet create)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        # Override create to ensure message is linked to a conversation
        conversation_id = request.data.get('conversation')
        if not conversation_id:
            return Response({"error": "Conversation ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
# Create your views here.
