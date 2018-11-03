from django.db import models
from django.utils import timezone

# Create your models here.

# Category start

class Category(models.Model):
    name = models.CharField(verbose_name='文章类别', max_length=20)

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name

# Category end            

# Tag start

class Tag(models.Model):
    name = models.CharField(verbose_name='文章标签', max_length=20)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# Tag end

# Blog start

class Blog(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='正文', default='')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    category = models.ForeignKey(Category, verbose_name='文章类别', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')

    class Meta:
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
    
# Blog end
