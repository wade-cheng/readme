# Generated by Django 5.0.6 on 2024-06-16 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_author_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='authors',
        ),
    ]