import factory
from chats.models import Chat

class RandomChatFactory(factory.Factory):
    class Meta:
        model = Chat