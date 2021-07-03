from django.db import models

# Create your models here.

class HelloWorld(models.Model): #Model을 상속받음
    text = models.CharField(max_length=255, null=False)
