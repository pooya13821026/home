# Generated by Django 3.2.19 on 2023-06-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('mobile', models.IntegerField(verbose_name='موبایل')),
                ('message', models.TextField(verbose_name='متن پیام')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال پیام')),
                ('response', models.TextField(verbose_name='پاسخ')),
                ('is_read', models.BooleanField(default=False, verbose_name='خوانده شده')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
    ]
