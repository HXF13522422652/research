from django.db import models

# Create your models here.
class UserInfo(models.Model):
    """员工表"""
    nid=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='员工表'

class Grade(models.Model):
    """班级表"""
    nid=models.BigAutoField(primary_key=True)
    title=models.CharField(verbose_name='班级名',max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '班级表'


class Student(models.Model):
    """学生表"""
    nid=models.BigAutoField(primary_key=True)
    user=models.CharField(verbose_name='学生名',max_length=30)
    pwd=models.CharField(max_length=32,)
    grade = models.ForeignKey(verbose_name='学生与班级关系',to='Grade')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = '学生表'


class Questionary(models.Model):
    """问卷表"""
    nid=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=32)

    grade = models.ForeignKey(verbose_name='和班级对应关系',to='Grade')
    creator=models.ForeignKey(verbose_name='创建者',to='UserInfo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '问卷表'


class Quesion(models.Model):
    """问题表"""
    nid=models.BigAutoField(primary_key=True)
    quesion=models.CharField(verbose_name='问题名',max_length=100)
    quesion_type=(
        (1,'打分'),
        (2,'单选'),
        (3,'评价')
    )
    tp=models.IntegerField(choices=quesion_type)
    naire=models.ForeignKey('Questionary',default=1)
    def __str__(self):
        return self.quesion

    class Meta:
        verbose_name = '问题表'


class One_choice(models.Model):

    """单选题选项表"""
    nid=models.BigAutoField(primary_key=True)
    name=models.CharField(verbose_name='选项名',max_length=32)
    score=models.IntegerField(null=True,default=True,verbose_name='选项对应的分值',)
    question=models.ForeignKey(to='Quesion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '单选题选项表'




class Answer(models.Model):
    """答案表"""
    nid=models.BigAutoField(primary_key=True)
    content=models.CharField(verbose_name='答案内容',max_length=260,null=True,blank=True)
    quesion = models.ForeignKey(to='Quesion')
    student=models.ForeignKey(to='Student')
    one_choice=models.ForeignKey(to='One_choice')
    val=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '答案表'