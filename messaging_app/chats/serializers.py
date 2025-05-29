from rest_framework import serializers
from chats.models import CustomUser, Conversation, Message

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']  # Add any other fields you want to expose


# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)  # Assuming sender is a FK to CustomUser

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp']


# Conversation Serializer with nested messages
class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)  # Assuming ManyToManyField
    messages = MessageSerializer(many=True, read_only=True)   # Assuming related_name='messages' on Message FK to Conversation

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'created_at', 'messages']
