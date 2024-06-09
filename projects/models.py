# projects/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", blank=True)
    exe_file = models.FileField(upload_to="project_downloads", blank=True)
    video_demo = models.FileField(blank=True, null=True)