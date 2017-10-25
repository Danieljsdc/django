from django.db import models
import django.utils.timezone as timezone

class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')
    content = models.TextField(null=True)
    add_temptime = models.DateTimeField('保存日期',default = timezone.now)
    mod_temptime = models.DateTimeField('修改日期',auto_now=True)


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username