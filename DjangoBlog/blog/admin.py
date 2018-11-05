from django.contrib import admin
from blog.models import Blog, Category, Tag, FriendUrl

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(FriendUrl)
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'create_time', 'modify_time']

admin.site.unregister(Blog)
admin.site.register(Blog, BlogAdmin)