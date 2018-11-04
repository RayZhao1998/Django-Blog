# Django-Blog

## Install & Run

推荐使用 virtualenv 创建虚拟环境

```
pip install -r requirements.txt
```

修改数据库配置 (`setting.py`)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DjangoBlogDB',
        'USER': '******',
        'PASSWORD': '******',
        'HOST': '127.0.0.1', # localhost
        'PORT': '3306',
    }
}
```

运行即可

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 待完成的功能

- [] 支持 RSS 订阅
- [x] 支持评论
- [] 博客首页文章布局 列表/网格 切换
- [] 后台添加友链
- [] Dark Mode
- [] 多 Markdown 主题更换
- [] 集成 Google 分析并在后台展示