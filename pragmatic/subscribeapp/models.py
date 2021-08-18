from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


class Subscription(models.Model):
    # 유저와 프로젝트 쌍이 하나가 되게
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        # 이 한쌍이 가지는 subscription은 오직하나만 존재
        unique_together = ('user', 'project')
