from rest_framework import serializers
from .models import Chat, Member, Attachment, Message

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'is_group_chat', 'topic', 'last_message', )

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('user', 'chat', 'last_message_count', 'last_message',)

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('user', 'chat', 'type', 'message',)

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('content', 'added_at', 'user', 'chat',)
