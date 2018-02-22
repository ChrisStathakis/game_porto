from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

MEDIAURL = 'https://s3.eu-west-2.amazonaws.com/levavour/media'


def project_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'project/%s/%s'%(instance.title, filename)


def images_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'project/images/%s/%s'%(instance.project_related.title, filename)


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


class ImageProductManager(models.Manager):
     def active(self):
        return super(ImageProductManager, self).filter(active=True)

     def post_related_and_active(self, post):
         return super(ImageProductManager, self).filter(active= True, project_related=post)

     def post_related(self, post):
         return super(ImageProductManager, self).filter(project_related=post)


class ProjectsManager(models.Manager):
    def active(self):
        return super(ProjectsManager, self).filter(active=True)


class ProjectCategory(models.Model):
    title = models.CharField(unique=True, max_length=255)

    class Meta:
        verbose_name_plural = '3. List of Categories.'

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=255, unique=True,)
    image = models.ImageField(upload_to=project_directory_path)
    short_description = models.CharField(max_length=100, help_text='The text appears on homepage')
    description = models.TextField()
    extra_info = models.TextField(help_text='About section', default='default')
    about_text = models.TextField(null=True, blank=True, help_text='No html needed, Converts always to caps')
    slug = models.SlugField(blank=True, null=True)
    seo_title = models.CharField(max_length=60, blank=True, null=True)
    seo_description = models.CharField(max_length=160, blank=True, null=True)
    seo_keywords = models.CharField(max_length=160, blank=True, null=True)
    active = models.BooleanField(default=True)
    my_query= ImageProductManager()
    objects = models.Manager()
    category = models.ForeignKey(ProjectCategory, null=True)
    image_background_page = models.ImageField(null=True, blank=True,upload_to=project_directory_path, help_text='Its for the background page cover, uf left black, it will appear black')
    css_background_color = models.CharField(max_length=50, null=True, blank=True, verbose_name='Page Background Color', help_text='Use hex color or colors like blue etc')
    css_background_color_menu = models.CharField(max_length=50, null=True, blank=True, verbose_name='Menu Background Color', help_text='Use hex color or colors like blue etc')
    href_color = models.CharField(max_length=50, null=True, blank=True, verbose_name='Href Color', help_text='Use hex color or colors like blue etc')
    css_font_color = models.CharField(max_length=50, null=True, blank=True, verbose_name='Font Color', help_text='Use hex color or colors like blue etc')
    css_font_style = models.CharField(max_length=50, verbose_name='Font Style', default='sans-serif', help_text='Use hex color or colors like blue etc')

    class Meta:
        verbose_name_plural = '1. List of Projects'
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('project', kwargs ={'slug':self.slug})
    def image_tag(self):
        return mark_safe('<img width="150px" height="150px" src="%s/%s" />' %(MEDIAURL, self.image))
    image_tag.short_description = 'Image'
    def image_tag_tiny(self):
        return mark_safe('<img width="50px" height="50px" src="%s/%s" />' %(MEDIAURL, self.image))
    image_tag.short_description = 'Image'
    def background_image_tag(self):
        return mark_safe('<img width="150px" height="150px" src="%s/%s" />' %(MEDIAURL, self.image))

    def additional_images_active(self):
        return ImageProject.my_query.post_related_and_active(post=self)
    def additional_images(self):
        return ImageProject.my_query.post_related(post=self)

class ImageProject(models.Model):
    title = models.CharField(max_length=60, blank=True)
    alt = models.CharField(max_length=60, null=True, blank=True)
    image = models.ImageField(upload_to=images_directory_path)
    text = models.TextField(blank=True, null=True, verbose_name='Optional description.')
    project_related = models.ForeignKey(Projects)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    my_query = ImageProductManager()

    class Meta:
        verbose_name_plural = '2. Gallery'

    def image_tag(self):
        return mark_safe('<img width="150px" height="150px" src="https://s3.eu-west-2.amazonaws.com/levavour/media/%s" />' %(self.image))
    def image_tag_tiny(self):
        return mark_safe('<img width="50px" height="50px" src="https://s3.eu-west-2.amazonaws.com/levavour/media/%s" />' %(self.image))
    image_tag_tiny.short_description = 'Image'

    def __str__(self):
        return self.title


class SkillProgress(models.Model):
    title = models.CharField(max_length=100, unique=True)
    percent = models.IntegerField(default=50)
    project_related = models.ForeignKey(Projects)
    color_bar = models.CharField(max_length=100, null=True, blank=True, help_text='Optional changes the color of the bar, Use hex colors to be sure.')

    class Meta:
        verbose_name_plural = '4. Skill Bar on About Page'

    def __str__(self):
        return self.title

