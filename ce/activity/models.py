from django.db import models

# Create your models here.

class Userinfo(models.Model):
    username = models.CharField('姓名',max_length=70,null=False)
    password=models.CharField('密码',max_length=200,null=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table='Userinfo'
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

