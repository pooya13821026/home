from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    categorys = models.CharField(max_length=10, verbose_name='دسته بندی')
    url_title = models.SlugField(max_length=200, db_index=True, verbose_name='url')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.categorys


class PropertyType(models.Model):
    types = models.CharField(max_length=20, verbose_name='نوع ملک')
    url_title = models.SlugField(max_length=200, db_index=True, verbose_name='url')

    class Meta:
        verbose_name = 'نوع'
        verbose_name_plural = 'نوع ملک'

    def __str__(self):
        return self.types


class State(models.Model):
    state = models.CharField(max_length=20, verbose_name='استان')

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'

    def __str__(self):
        return self.state


class Estate(models.Model):
    title = models.CharField(max_length=30, verbose_name='عنوان')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, verbose_name='نوع ملک')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='استان')
    year_of_construction = models.PositiveIntegerField(verbose_name='سال ساخت')
    address = models.CharField(max_length=100, verbose_name='ادرس ملک')
    Meterage = models.PositiveIntegerField(verbose_name='متراژ')
    image = models.ImageField(upload_to='estate', verbose_name='عکس', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='قیمت کل')
    create_time = models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت', editable=False)
    slug = models.SlugField(verbose_name='عنوان در url', max_length=200, allow_unicode=True)
    special = models.BooleanField(verbose_name='ویژه', default=False)

    class Meta:
        verbose_name = 'ملک'
        verbose_name_plural = 'املاک'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('estate_deteil', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
