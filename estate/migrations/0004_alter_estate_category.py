# Generated by Django 3.2.19 on 2023-06-26 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0003_auto_20230626_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.category', verbose_name='دسته بندی'),
        ),
    ]