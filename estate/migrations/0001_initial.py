# Generated by Django 3.2.19 on 2023-06-19 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=10, verbose_name='نوع ملک')),
            ],
            options={
                'verbose_name': 'نوع',
                'verbose_name_plural': 'نوع ملک ها',
            },
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='عنوان')),
                ('Meterage', models.PositiveIntegerField(verbose_name='متراژ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='estate', verbose_name='عکس')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت کل')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت')),
                ('slug', models.SlugField(max_length=200, verbose_name='عنوان در url')),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.propertytype', verbose_name='نوع ملک')),
            ],
            options={
                'verbose_name': 'ملک',
                'verbose_name_plural': 'املاک',
            },
        ),
    ]