# Generated by Django 4.2.13 on 2024-06-09 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_exe_file_project_video_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='video_demo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]