# Generated by Django 3.2.19 on 2023-07-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0013_alter_estate_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url_title',
            field=models.SlugField(blank=True, max_length=200, null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='propertytype',
            name='url_title',
            field=models.SlugField(blank=True, max_length=200, null=True, verbose_name='url'),
        ),
    ]
