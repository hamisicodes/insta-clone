# Generated by Django 3.0.6 on 2020-06-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0011_auto_20200601_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='../static/photos/profile.jpeg', upload_to='users/'),
        ),
    ]
