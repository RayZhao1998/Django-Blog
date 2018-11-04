from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from blog.models import Blog, Category, Tag, Comment
from pure_pagination import PageNotAnInteger, Paginator
import markdown2
from blog.forms import CommentForm

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

        all_comments = Comment.objects.all().filter(blog_id=blog_id)
        return render(request, 'blog-detail.html', {
            'blog': blog,
            'all_comments': all_comments,
        })

class AddCommentView(View):
    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail"}', content_type="application/json")