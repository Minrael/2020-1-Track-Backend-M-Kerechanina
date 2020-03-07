from user.views import profile_user, contacts
from django.urls import path

urlpatterns = [
  #path('<int:pk>', chat_list, name='chat_list'),
  path('profile/', profile_user, name='profile_user'),
  path('contacts/', contacts, name='contacts'),
]