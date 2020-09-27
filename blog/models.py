from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class ExtraBlogHome(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post_type = models.CharField(max_length=50)
    hashtags = models.CharField(max_length=20, blank=True)
    author = models.CharField(max_length=20)
    comments_count = models.TextField()
    post_old_or_new = models.BooleanField(default=False )

    def __str__(self):
        return self.title


class VideoPost(models.Model):
    video = models.FileField(upload_to='videos/',null=True,verbose_name='')


class SinglePost(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    admin = models.CharField(max_length=50)
    description = models.TextField()
    categories = models.CharField(max_length=30,null=True)

   
    def __str__(self):
        return self.title

class CategoriesFiled(models.Model):
    category =models.CharField(max_length=50)


    def __str__(self):
        return self.category
# class RealatedPost(models.Model):
#     realatedPost_img = models.ImageField(upload_to='images/')
#     relrealatedPost_title = models.CharField(max_length=100)