from django.db import models


class SiteSetting(models.Model):
    title = models.CharField(max_length=20, verbose_name='عنوان تنظیمات')
    logo = models.ImageField(upload_to='logo', verbose_name='لوگو')
    phone = models.PositiveIntegerField(verbose_name='موبایل')
    email = models.EmailField(verbose_name='ایمیل')
    address = models.CharField(max_length=30, verbose_name='ادرس')
    facebook_url = models.URLField(max_length=500, verbose_name='فیسبوک', null=True, blank=True)
    aparat_url = models.URLField(max_length=500, verbose_name='آپارات', null=True, blank=True)
    instagram_url = models.URLField(max_length=500, verbose_name='اینستاگرام')
    telegram_url = models.URLField(max_length=500, verbose_name='تلگرام')
    youtube_url = models.URLField(max_length=500, verbose_name='یوتیوب', null=True, blank=True)
    whatsapp_url = models.URLField(max_length=500, verbose_name='واتساپ', null=True, blank=True)
    main_setting = models.BooleanField(verbose_name='تنظیمات اصلی', default=False)

    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.title


class FooterLinkTitle(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان لینک فوتر')

    class Meta:
        verbose_name = 'عنوان لینک فوتر'
        verbose_name_plural = 'عناوین لینکهای فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='لینک فوتر')
    url_title = models.URLField(max_length=500, verbose_name='آدرس url لینک')
    footer_link_title = models.ForeignKey(to=FooterLinkTitle, on_delete=models.CASCADE,
                                          verbose_name='عنوان سردسته لینک')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینکهای فوتر'

    def __str__(self):
        return self.title


class HomeBaner(models.Model):
    img = models.ImageField(upload_to='home_baner', verbose_name='بنر اول صفحه اصلی')
    title = models.CharField(verbose_name='عنوان', max_length=30)
    des = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنر صفحه اصلی'
