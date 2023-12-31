# Generated by Django 3.2.19 on 2023-06-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=15, verbose_name='عنوان اصلی 1')),
                ('subject', models.TextField(verbose_name='متن عنوان اصلی')),
                ('title2', models.CharField(max_length=25, verbose_name='عنوان اصلی 2')),
                ('subtitle1', models.CharField(max_length=30, verbose_name='عنوان فرعی 1')),
                ('subtitle2', models.CharField(max_length=30, verbose_name='عنوان فرعی 2')),
                ('subtitle3', models.CharField(max_length=30, verbose_name='عنوان فرعی 3')),
                ('subject1', models.TextField(verbose_name='متن عنوان فرعی 1')),
                ('subject2', models.TextField(verbose_name='متن عنوان فرعی 2')),
                ('subject3', models.TextField(verbose_name='متن عنوان فرعی 3')),
                ('img', models.ImageField(upload_to='about', verbose_name='عکس')),
                ('title3', models.CharField(max_length=30, verbose_name='عنوان اصلی 3')),
                ('sub_title1', models.CharField(max_length=30, verbose_name='عنوان فرعی 1')),
                ('sub_title2', models.CharField(max_length=30, verbose_name='عنوان فرعی 2')),
                ('sub_title3', models.CharField(max_length=30, verbose_name='عنوان فرعی 3')),
                ('sub_ject1', models.TextField(verbose_name='متن عنوان فرعی 1')),
                ('sub_ject2', models.TextField(verbose_name='متن عنوان فرعی 2')),
                ('sub_ject3', models.TextField(verbose_name='متن عنوان فرعی 3')),
                ('main', models.BooleanField(default=False, verbose_name='فعال/غیر فعال')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'تنظیمات درباره ما',
            },
        ),
    ]
