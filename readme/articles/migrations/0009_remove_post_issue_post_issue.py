# Generated by Django 5.0.6 on 2024-06-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_issue_num_alter_issue_vol_remove_post_issue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='issue',
        ),
        migrations.AddField(
            model_name='post',
            name='issue',
            field=models.ManyToManyField(related_name='posts', to='articles.issue'),
        ),
    ]
