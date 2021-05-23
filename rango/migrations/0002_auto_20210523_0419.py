# Generated by Django 3.2.3 on 2021-05-23 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
