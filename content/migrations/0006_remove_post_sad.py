# Generated by Django 4.2.2 on 2023-06-18 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_post_saved_user_post_saved_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sad',
        ),
    ]
