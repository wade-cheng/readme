# Generated by Django 5.0.6 on 2024-06-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0028_alter_uploadedimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]
