# Generated by Django 5.1.3 on 2024-11-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_book_price_alter_book_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
