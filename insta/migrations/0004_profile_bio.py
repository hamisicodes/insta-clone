# Generated by Django 3.0.6 on 2020-05-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Hello everyone amusing insta-clone'),
        ),
    ]