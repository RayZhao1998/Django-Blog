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
    is_top = models.BooleanField(verbose_name="是否置顶", default=False)
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

# Comment start

class Comment(models.Model):
    nickname = models.CharField(verbose_name="昵称", max_length=20, default="匿名")
    content = models.CharField(verbose_name="内容", max_length=300)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    blog = models.ForeignKey(Blog, verbose_name="博客", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "博客评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:10]
# Comment end

# FriendUrl start
class FriendUrl(models.Model):
    nickname = models.CharField(verbose_name="昵称", max_length=100)
    url = models.CharField(verbose_name="链接", max_length=100)

    class Meta:
        verbose_name = "友链"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname
# FriendUrl end