from django.db import models
from django.conf import settings

from django.contrib.contenttypes.models import ContentType

# Create your models here.


def post_upload():
    return '/post_images'

class PostTags(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class PostCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)
    content = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Title')
    image = models.FileField(upload_to='post_images/', verbose_name='Image - not used atm', blank=True)
    lead_content = models.TextField(null=True, blank=True, verbose_name='Name of the Site')
    content = models.TextField(verbose_name='Short description or Intro')
    href = models.CharField(max_length=200)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    #publish = models.DateField(auto_now=True, auto_now_add=False)
    #updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True,null=True, blank=True, allow_unicode=True, verbose_name='Slug - Dont bother with that ')
    #seo = models.CharField(max_length=100, blank=True)
    #meta_description = models.CharField(max_length=100, blank=True)
    #category = models.ForeignKey(PostCategory, null=True)


    def __str__(self):
        return self.title

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type