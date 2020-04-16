from chats.views import (
  index_page,
  chat_list,
  chat_page,
  user_chat_list,
  send_message,
  chat_message_list,
  search_user,
  send_message_with_html,
  ChatView,
  ChatsViewSet,
  MessageViewSet,
)
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'chats', ChatsViewSet)
router.register(r'chat_message_list_2', MessageViewSet)

urlpatterns = [
  #path('<int:pk>', chat_list, name='chat_list'),
  path('', index_page, name='index_page'),
  path('chat_list/', chat_list, name='chat_list'),
  path('user_chat_list/<int:user_id>', user_chat_list, name='user_chat_list'),
  path('chat_page/<int:chat_id>', chat_page, name='chat_page'),
  path('send_message/', send_message, name='send_message'),
  path('send_message_with_html/', send_message_with_html, name='send_message_with_html'),
  path('chat_message_list/', chat_message_list, name='chat_message_list'),
  path('search_user/', search_user, name='search_user'),
  path('c/', ChatView.as_view()),
] + router.urls