# Generated by Django 5.1.3 on 2024-11-30 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0007_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]
