from django.contrib import admin
from .models import Post, Comment, Category, Places , People, Comment2
from django.conf import settings
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Places) 
admin.site.register(People) 
admin.site.register(Comment2) 

 