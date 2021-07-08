from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)  #프로필 사진을 서버에 저장되게
    nickname = models.CharField(max_length=20, unique=True, null=True) #unique: 중복되지 않게
    message = models.CharField(max_length=100, null=True)
