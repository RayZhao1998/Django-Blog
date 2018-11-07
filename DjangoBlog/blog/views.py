from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core import serializers
from blog.models import Blog, Category, Tag, Comment
from pure_pagination import PageNotAnInteger, Paginator
import markdown2
import json
from blog.forms import CommentForm

# Create your views here.

class IndexView(View):
    def get(self, request):
        all_blogs = Blog.objects.order_by('-is_top', '-id')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blogs, 5, request=request)
        all_blogs = p.page(page)
        for blog in all_blogs.object_list:
            description_end_index = blog.content.find("<!-- more -->")
            blog.content = blog.content[:description_end_index]
            blog.content = markdown2.markdown(blog.content, extras=['fenced-code-blocks'])

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

class GetCategoryView(View):
    def get(self, request):
        categories = serializers.serialize("json", Category.objects.all())
        return HttpResponse(json.dumps(categories), content_type="application/json")

class AddCommentView(View):
    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail"}', content_type="application/json")

class CategoryBlogListView(View):
    def get(self, request, category):
        category = Category.objects.filter(name=category)
        cat_id = category.values("id")[0]["id"]
        blogs = Blog.objects.all().filter(category_id=cat_id)
        return render(request, 'category-blog-list.html', {
            'blogs': blogs,
        })