# Generated by Django 3.2.19 on 2023-06-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0004_alter_estate_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
    ]
