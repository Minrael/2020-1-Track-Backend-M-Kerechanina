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
        self.chat1 = Chat.objects.create(topic='chat1', is_group_chat=False)
        self.user1 = RandomUserFactory.create()
        self.user1.save()
        self.member = Member.objects.create(
            user=self.user1,
            chat=self.chat1,
            new_messages_count=0
        )

    def test_chat_message_list_is_empty(self):
        response = self.client.get('/chats/chat_message_list/')
        content = json.loads(response.content)
        self.assertFalse(content['messages'])

    def test_chat_message_list(self):
        self.message1 = Message.objects.create(content='Hey!', chat=self.chat1, user=self.user1, added_at = timezone.now())
        self.message2 = Message.objects.create(content='He', chat=self.chat1, user=self.user1, added_at = timezone.now())
        self.message3 = Message.objects.create(content='Bye!', chat=self.chat1, user=self.user1, added_at = timezone.now())
        response = self.client.get('/chats/chat_message_list/')
        content = json.loads(response.content)
        self.assertEqual(len(content['messages']), 3)

    def test_send_message(self):
        response = self.client.post('/chats/send_message/', {'content':'Hey!', 'chat': self.chat1.id, 'user': self.user1.id})
        messages = Message.objects.all().values('content')
        self.assertEqual(list(messages), [{'content': 'Hey!'}] )

    def test_send_message_and_reseve(self):
        response_1 = self.client.post('/chats/send_message/', {'content':'Hey!', 'chat': self.chat1.id, 'user': self.user1.id})
        response_2 = self.client.get('/chats/chat_message_list/')
        content = json.loads(response_2.content)
        self.assertDictEqual(content, {"messages": [{"content": "Hey!"}]})


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
