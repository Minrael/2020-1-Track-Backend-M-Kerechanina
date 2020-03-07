from django.db import models
from user.models import User

class Chat(models.Model):
    topic = models.CharField(max_length=32, null=False, default='topic1')
    is_group_chat = models.BooleanField(default=False)
    last_messege = models.ForeignKey(to='Message', on_delete=models.CASCADE, null=True, related_name = 'last_messege_id')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

class Message(models.Model):
    content = models.TextField(max_length=300)
    added_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    new_messages_count = models.IntegerField()
    last_message = models.ForeignKey('Message', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

class Attachment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    type = models.CharField(max_length = 64)

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

