
from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta: #유저랑 유저 프로젝트 쌍이 하나여야 함
        unique_together = ('user', 'project')