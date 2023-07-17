from django.db import models


class ContactUs(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    mobile = models.CharField(max_length=11, verbose_name='موبایل')
    message = models.TextField(verbose_name='متن پیام')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال پیام')
    response = models.TextField(verbose_name='پاسخ')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.full_name
