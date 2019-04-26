from django.db import models


class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (1, '男'),
        (1, '男'),
    ]
    STATUS_ITEMS = [
        (0, '中请'),
        (1, '通过'),
        (2, '拒绝')
    ]

    name = models.CharField(max_length=128, verbose_name='姓名')
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name='性别')
    profession = models.CharField(max_length=128, verbose_name='职业')
    email = models.EmailField(verbose_name='email')
    qq = models.CharField(max_length=128, verbose_name='QQ')
    phone = models.CharField(max_length=128, verbose_name='电话')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')
    status = models.IntegerField(choices=STATUS_ITEMS,default=0,verbose_name='审核状态')

    class Meta:

        db_table = 'student'
        verbose_name=verbose_name_plural='学院信息'

    def __str__(self):
        return f'<Student:{self.name}>'


    @classmethod
    def get_all(cls):
        return cls.objects.all()
