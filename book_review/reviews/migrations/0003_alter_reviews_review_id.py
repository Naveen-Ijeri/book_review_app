# Generated by Django 5.1.2 on 2024-10-21 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_rename_book_id_reviews_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review_id',
            field=models.CharField(default='895b1531-2137-4fb7-809c-f52d1b26a7e0', primary_key=True, serialize=False),
        ),
    ]
