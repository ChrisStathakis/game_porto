from django.db import models
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
import os

# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

MEDIAURL = 'https://s3.eu-west-2.amazonaws.com/levavour/media'

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'art_{0}/{1}'.format(instance.project_related.title, filename)

def art_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'art/image/{0}/{1}'.format(instance.title, filename)

def art_background_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'art/image/back/{0}/{1}'.format(instance.title, filename)

def validate_size(value):
    if value.size > 1024*1024:
        raise ValidationError('This file is bigger than 1 mb')
    return value

def validate_hex_color(value):
    # function that checks if the text used is using hex color
    value = str(value)
    if not value.startswith('#'):
        raise ValidationError(
            _('%(value)s have to start with #'),
            params={'value': value},
        )
    if len(value) > 6:
        raise ValidationError(
            _('Your length is need to be less than 6.')
        )

class ArtManager(models.Manager):
    def active(self):
        return super(ArtManager, self).filter(active=True)


class Art(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(help_text='The image thats appears on homepage',
                              upload_to=art_directory_path,
                              validators=[validate_size, ])
    short_description = models.CharField(max_length=100, help_text='The text appears on homepage, no use of html')
    description = models.TextField(blank=True, null=True, help_text='The full description for the art page. HTML USE')
    slug = models.SlugField(blank=True, null=True, help_text='Dont change it!!')
    seo_title = models.CharField(max_length=60, blank=True, null=True)
    seo_description = models.CharField(max_length=160, blank=True, null=True, help_text='The text thats appears on google for the site description. If left null will get the first 160 characters from description.')
    seo_keywords = models.CharField(max_length=160, blank=True, null=True, help_text='Use words that appears oon text, synonyms and no spam for better use.')
    active = models.BooleanField(default=True)
    my_query= ArtManager()
    objects = models.Manager()
    image_background_page = models.ImageField(null=True, blank=True, upload_to=art_background_directory_path,
                                              help_text='Its for the background page cover, uf left black, it will appear black',
                                              validators=[validate_size, ])
    css_background_color = models.CharField(max_length=50,
                                            null=True,
                                            blank=True,
                                            verbose_name='Background Color Page',
                                            help_text='Use hex color or colors like blue etc',

                                            )
    css_background_color_menu = models.CharField(max_length=50,
                                            null=True,
                                            blank=True,
                                            verbose_name='Background Color Menu',
                                            help_text='Use hex color or colors like blue etc',

                                            )
    href_color = models.CharField(max_length=50,
                                            null=True,
                                            blank=True,
                                            verbose_name='Href etc',
                                            help_text='Use hex color or colors like blue etc',

                                            )
    css_font_color = models.CharField(max_length=50,
                                      null=True,
                                      blank=True,
                                      verbose_name='Font Color',
                                      help_text='Use hex color or colors like blue etc',
                                      )
    css_font_style = models.CharField(max_length=50,
                                      verbose_name='Font Style',
                                      default='sans-serif',
                                      help_text='Use hex color or colors like blue etc',
                                      )
    class Meta:
        verbose_name_plural = '1. List of Arts'

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('choosed_art', kwargs ={'slug':self.slug})

    def image_tag(self):
        return mark_safe('<img width="150px" height="150px" src="%s/%s" />' %(MEDIAURL, self.image))
    def image_tag_tiny(self):
        return mark_safe('<img width="50px" height="50px" src="%s/%s" />' %(MEDIAURL, self.image))
    image_tag_tiny.short_description = 'Image'
    def background_image_tag(self):
        return mark_safe('<img width="150px" height="150px" src="%s/%s" />' %(MEDIAURL, self.image_background_page))

    def additional_images_active(self):
        return ImageArt.my_query.post_related_and_active(post=self)
    def additional_images(self):
        return ImageArt.my_query.post_related(post=self)

class ImageArtManager(models.Manager):
     def active(self,):
        return super(ImageArtManager, self).filter(active=True)
     def post_related_and_active(self, post):
         return super(ImageArtManager, self).filter(active= True, project_related = post)
     def post_related(self, post):
         return super(ImageArtManager, self).filter(project_related = post)

class ImageArt(models.Model):
    title = models.CharField(max_length=60, blank=True)
    alt = models.CharField(max_length=60, null=True, blank=True)
    project_related = models.ForeignKey(Art, help_text='Pick the project image is related')
    image = models.ImageField(upload_to=user_directory_path)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    my_query = ImageArtManager()

    class Meta:
        verbose_name_plural ='2. Gallery'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img width="150px" height="150px" src="https://s3.eu-west-2.amazonaws.com/levavour/media/%s" />' %(self.image))
    def image_tag_tiny(self):
        return mark_safe('<img width="50px" height="50px" src="https://s3.eu-west-2.amazonaws.com/levavour/media/%s" />' %(self.image))
    image_tag_tiny.short_description = 'Image'
