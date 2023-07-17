from django.db import models


class About(models.Model):
    title1 = models.CharField(max_length=15, verbose_name='عنوان اصلی 1')
    subject = models.TextField(verbose_name='متن عنوان اصلی')
    img1 = models.ImageField(upload_to='about', blank=True)
    img2 = models.ImageField(upload_to='about', blank=True)

    title2 = models.CharField(max_length=25, verbose_name='عنوان اصلی 2')
    subtitle1 = models.CharField(max_length=30, verbose_name='عنوان فرعی 1')
    subtitle2 = models.CharField(max_length=30, verbose_name='عنوان فرعی 2')
    subtitle3 = models.CharField(max_length=30, verbose_name='عنوان فرعی 3')
    subject1 = models.TextField(verbose_name='متن عنوان فرعی 1')
    subject2 = models.TextField(verbose_name='متن عنوان فرعی 2')
    subject3 = models.TextField(verbose_name='متن عنوان فرعی 3')

    title3 = models.CharField(max_length=30, verbose_name='عنوان اصلی 3')
    sub_title1 = models.CharField(max_length=30, verbose_name='عنوان فرعی 1')
    sub_title2 = models.CharField(max_length=30, verbose_name='عنوان فرعی 2')
    sub_title3 = models.CharField(max_length=30, verbose_name='عنوان فرعی 3')
    sub_ject1 = models.TextField(verbose_name='متن عنوان فرعی 1')
    sub_ject2 = models.TextField(verbose_name='متن عنوان فرعی 2')
    sub_ject3 = models.TextField(verbose_name='متن عنوان فرعی 3')
    main = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'تنظیمات درباره ما'

    def __str__(self):
        return self.title1
