# Generated by Django 5.0.6 on 2024-06-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_author_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(),
        ),
    ]
