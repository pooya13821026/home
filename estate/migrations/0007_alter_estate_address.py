# Generated by Django 3.2.19 on 2023-06-26 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0006_estate_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='address',
            field=models.CharField(max_length=100, verbose_name='ادرس ملک'),
        ),
    ]
