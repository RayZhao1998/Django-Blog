from django.shortcuts import render
from django.views import View
from blog.models import Blog, Category, Tag
from pure_pagination import PageNotAnInteger, Paginator

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