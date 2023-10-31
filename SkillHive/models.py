
from django.db import models

class SkillHive(models.Model):
    objects = None
    title = models.CharField(max_length=100,default=None)
    description = models.TextField(max_length=10000,default=None)
    cover_photo = models.ImageField(upload_to='course_covers/', default=None)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(SkillHive, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    video = models.FileField(upload_to='videos/', null=True, blank=True)


    def __str__(self):
        return self.title