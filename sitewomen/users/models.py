from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")


# class Profile(models.Model):
#     user = models.OneToOneField('User', on_delete=models.CASCADE)
#     photo = models.ImageField(upload_to='users/%Y/%m/', blank=True, default='users/default.jpg',
#                               verbose_name='Изображение')
#     date_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')


