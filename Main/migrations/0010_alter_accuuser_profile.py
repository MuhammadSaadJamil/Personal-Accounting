# Generated by Django 4.0.1 on 2022-01-26 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_accuuser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accuuser',
            name='profile',
            field=models.ImageField(default='user.png', upload_to='profile/'),
        ),
    ]