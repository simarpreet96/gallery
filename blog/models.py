from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True, null=True)
    image = models.ImageField( upload_to='images/')
    published_date = models.DateTimeField(auto_now=True)
    approved_post = models.BooleanField(default=False) 

    def __str__(self):
        return self.title
    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,related_name='children', db_index=True)
    slug = models.SlugField()

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'categories'

    
    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class People(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image_people = models.ImageField()
    published_date = models.DateTimeField(auto_now=True)
    approved_post = models.BooleanField(default=False) 

    def __str__(self):
        return self.title


class Places(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image_places = models.ImageField()
    published_date = models.DateTimeField(auto_now=True)
    approved_post = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

class Comment2(models.Model):
    places = models.ForeignKey('blog.Places', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
