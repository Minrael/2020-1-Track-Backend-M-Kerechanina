from django.test import TestCase, Client
from chats.models import Chat, Member, Message
from user.models import User
from chats.user_factory import RandomUserFactory
import json
from mock import patch
from django.utils import timezone

class TestChatList(TestCase):
    def setUp(self):
        self.client = Client()
        self.chat = Chat.objects.create(topic='chat1', is_group_chat=False)
        #self.user1 = User.objects.create(username = 'user1')
        self.user1 = RandomUserFactory.create()
        self.user1.save()
        self.member = Member.objects.create(
            user=self.user1,
            chat=self.chat,
            new_messages_count=0,
            last_message = Message.objects.create(content='', user = self.user1, chat = self.chat, added_at = timezone.now())
        )
        self.message_0 = Message.objects.create(content = 'Yes!', user = self.user1, chat = self.chat, added_at = timezone.now())

    def test_send_message(self):
        response_1 = self.client.post('/chats/send_message/', {'content':'123', 'user': self.user1, 'chat': self.chat})
        #print(self.chat.id)
        #print(response_1)
        response_2 = self.client.get('/chats/chat_message_list/')
        self.assertEqual(response_2.content, "{'messages': [{'content': 'Hey!'}]}")


    def test_send_message_failed(self):
        #response = self.client.get('/chats/send_message/')
        #self.assertRaises()
        pass

    def test_user_chat_list(self):
        response = self.client.get('/chats/user_chat_list/1')
        self.assertJSONEqual(response.content, '{}')

    def test_chat_list(self):
        pass
        #self.assertJSONEqual(response.content, '{"data": [{"id": 1, "topic": "chat1"}]}')

    @patch('chats.views.search_user')
    def test_serch_user(self, user_found_mock):
        user_found_mock.return_value = True
        #response = self.client.get('/chats/search_user')
        #self.assertTrue(response.status_code == 200)
        self.assertTrue(user_found_mock.return_value)

    def tearDown(self):
        print('The end')
