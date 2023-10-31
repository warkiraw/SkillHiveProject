# Generated by Django 4.2.6 on 2023-10-24 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkillHive', '0003_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='video_url',
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]