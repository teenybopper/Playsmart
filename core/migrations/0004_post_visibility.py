# Generated by Django 4.2.5 on 2023-10-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_userprofile_followers_userprofile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('public', 'public'), ('Followers', 'Followers'), ('Only Me', 'Only Me')], default='public', max_length=20),
        ),
    ]
