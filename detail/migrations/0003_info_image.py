# Generated by Django 4.2.5 on 2023-10-19 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0002_rename_position_info_skill_remove_info_skills_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='pfp_images'),
        ),
    ]
