from django.contrib import admin
from chats.models import Chat
from user.models import User

class ChatsAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chat, ChatsAdmin)
admin.site.register(User, UserAdmin)
