from chats.views import index_page, chat_list, chat_page
from django.urls import path

urlpatterns = [
  #path('<int:pk>', chat_list, name='chat_list'),
  path('', index_page, name='index_page'),
  path('chat_list/', chat_list, name='chat_list'),
  path('chat_page/<int:chat_id>', chat_page, name='chat_page'),
]