from django.db import models


class Project(models.Model):
    # media/project 에 가는 것
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateField(auto_now=True, null=True)
