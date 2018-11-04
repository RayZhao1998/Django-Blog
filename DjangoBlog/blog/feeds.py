from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Blog
import markdown2

class BlogRssFeed(Feed):
    title = "忍者小屋"
    link = "/rss/"
    def items(self):
        return Blog.objects.all()
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        item.content = markdown2.markdown(item.content, extras=['fenced-code-blocks'])
        return item.content
    def item_link(self, item):
        return reverse('blog_id', args=[item.id,])