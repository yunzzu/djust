
from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    #on_delete: 회원 탈퇴를 했을 때 게시물이 사라지지 않고 '알 수 없음' 같이 나오게

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)  #생성일자
