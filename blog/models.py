from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from account.models import MyUser


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان وبلاگ')
    short_description = models.TextField(verbose_name='توضیح کوتاه')
    img = models.ImageField(upload_to='blog', verbose_name='عکس')
    subject1 = models.TextField(verbose_name='موضوع 1')
    subtext1 = models.TextField(verbose_name='متن 1')
    subject2 = models.TextField(verbose_name='موضوع 2')
    subtext2 = models.TextField(verbose_name='متن 2')
    create_time = models.DateTimeField(auto_now=True, editable=False, verbose_name='زمان انتشار')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url', allow_unicode=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='نویسنده', editable=False)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_deteil', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('BlogComment', on_delete=models.CASCADE, verbose_name='والد', null=True,
                               blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='کاربر')
    comment_text = models.TextField(verbose_name='متن نظر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت', editable=False)
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return str(self.user)
