from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


# class model for caegories
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("Category_detail", kwargs={"pk": self.pk})
        return reverse("hom")


# Create your models here.
class Poster(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title_tag = models.CharField(max_length=255,default="")
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255, default="click above to read the article")
    # body = models.TextField(max_length=2500)
    body = RichTextField(blank=True, null=True)
    Post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name = 'Blog_post')
    # unlikes = models.ManyToManyField(User, related_name = 'unBlog_post')

    def __str__(self):
        return self.title + '|' + str(self.author)
    

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})
    
    # Count the no. of likes 
    def total_likes(self):
        return self.likes.count()
    
    # def total_unlikes(self):
    #     return self.unlikes.count()


class Comment(models.Model):
    post = models.ForeignKey('Poster',on_delete=models.CASCADE ,related_name ="comments")
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s-%s'%(self.post.title, self.name)
    

class Profile(models.Model):
    author_name  = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    profilepic = models.ImageField(null=True,blank=True, upload_to="images/profile", height_field=None, width_field=None, max_length=None)
    bio = models.TextField(default="" , null=True)
    web_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    insta_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.author_name)
    