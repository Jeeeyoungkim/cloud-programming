# Generated by Django 4.2.2 on 2023-06-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_is_sad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='/static/assets/cloud_3d.png', upload_to='user'),
        ),
    ]
