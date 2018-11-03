from django.shortcuts import render
from django.views import View
from blog.models import Blog, Category, Tag
from pure_pagination import PageNotAnInteger, Paginator
import markdown2

# Create your views here.

class IndexView(View):
    def get(self, request):
        all_blogs = Blog.objects.all().order_by('-id')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blogs, 5, request=request)
        all_blogs = p.page(page)

        return render(request, 'index.html', {
            'all_blogs': all_blogs,
        })

class BlogDetailView(View):
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        blog.content = markdown2.markdown(blog.content, extras=['fenced-code-blocks'])
        return render(request, 'blog-detail.html', {
            'blog': blog,
        })