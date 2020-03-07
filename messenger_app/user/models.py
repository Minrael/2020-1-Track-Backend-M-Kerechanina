from django.db import models
from django.contrib.auth.models import AbstractUser

#user.model
class User(AbstractUser):
    avatar = models.ImageField(null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

