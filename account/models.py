from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar_user', verbose_name='عکس پروفایل', null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name='شماره موبایل')
    bio = models.TextField(verbose_name='بیوگرافی', null=True, blank=True)
    addres = models.CharField(max_length=50, verbose_name='ادرس', null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'
