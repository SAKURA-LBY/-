from django.db import models

# Create your models here.
class book_bookinfo(models.Model):

    title = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    isDelete = models.IntegerField()
    class Meta:
        db_table = 'book_bookinfo'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.title

class book_heroinfo(models.Model):

    hname = models.CharField(max_length=20)
    hgender = models.IntegerField(max_length=1)
    isDelete = models.IntegerField(max_length=1)
    hcontent = models.CharField(max_length=200)
    hbook_id = models.ForeignKey(book_bookinfo,on_delete=models.CASCADE)
    class Meta:
        db_table = 'book_heroinfo'  # 指明数据库表名
        verbose_name = '英雄'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.hname