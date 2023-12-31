# Generated by Django 3.2.19 on 2023-07-31 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0016_welfareamenities'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='estate',
            name='room',
            field=models.PositiveIntegerField(default=0, verbose_name='تعداد اتاق'),
        ),
        migrations.AddField(
            model_name='estate',
            name='wc',
            field=models.PositiveIntegerField(default=1, verbose_name='تعداد سرویس بهداشتی'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='title',
            field=models.CharField(db_index=True, max_length=30, verbose_name='عنوان'),
        ),
    ]
