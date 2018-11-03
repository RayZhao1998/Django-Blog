from django.shortcuts import render
from django.views import View
from blog.models import Blog, Category, Tag

# Create your views here.

class IndexView(View):
    def get(self, request):
        all_blogs = Blog.objects.all().order_by('-id')
        return render(request, 'index.html', {
            'all_blogs': all_blogs,
        })