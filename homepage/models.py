from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.

def upload_photo(instance,filename ):
    return 'homepage/{0}/{1}'.format(instance.title, filename)

class Welcome_page(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(unique=True, max_length=100, )
    logo = models.ImageField(upload_to=upload_photo)
    second_banner = models.ImageField(upload_to=upload_photo, null= True, help_text='')
    my_skills_section_message = models.CharField(max_length=160,
                                                 default='Would you like to know more or just discuss something?',
                                                 help_text='NO HTML here.')
    #personal_photo = models.ImageField(upload_to='personal_photo/')
    projects_section_message = models.CharField(max_length=160,
                                                 default='My works so far',
                                                 help_text='NO HTML here.')
    art_section_message = models.CharField(max_length=160,
                                                 default='See my demo sites and the future apps.',
                                                 help_text='NO HTML here.')
    blog_section_message = models.CharField(max_length=160,
                                                 default="See our latest posts in <a href='www.vavourasblog.com!'>www.vavourasblog.com!</a>",
                                                 help_text='USE HTML here.')
    seo_title = models.CharField(max_length=60, null=True, blank=True, help_text='Dont change it!')
    seo_keywords = models.CharField(max_length=160, null= True, blank=True, help_text='Use words that appears oon text, synonyms and no spam for better use.')
    seo_description = models.CharField(max_length=160, null= True, blank=True, help_text='The text thats appears on google for the site description.')

    about_me = models.CharField(max_length=20, default='ABOUT ME')
    about_me_image = models.ImageField(upload_to=upload_photo, null=True)
    personal_photo = models.ImageField(upload_to=upload_photo, null=True)

    my_skills = models.CharField(max_length=20, default='MY SKILLS')
    project = models.CharField(max_length=20, default='Projects')

    left_text = models.TextField(default='Left part')
    center_text = models.TextField(default='Center part')
    right_text = models.TextField(default='Right part')

    #css
    body_background_color = models.CharField(max_length=10, default='', verbose_name='Background Color of all page' )
    menu_hover_color = models.CharField(max_length=10, default='', verbose_name='Menu hover color')
    skills_color_primary = models.CharField(max_length=10, default='#13836c' , verbose_name='Service Primary color', help_text='Change the color on service section')
    skills_color_secondary = models.CharField(max_length=10, default='#45b59e', verbose_name='Service Secondary  Color')

    main_color_fonts = models.CharField(max_length=10, default='#f4d9d9')
    secondary_color_font = models.CharField(max_length=10, default='#f4d9d9', verbose_name='Menu color and paragraphs etc')
    third_color_font = models.CharField(max_length=10, default='#f4d9d9', null=True, blank=True, help_text='You control here the titles of projects and the urls.', verbose_name='Ahref color controller')

    class Meta:
        verbose_name_plural = '1.Anything about index page'

    def __str__(self):
        return self.title

    def logo_tag(self):
        return mark_safe('<img src="https://s3.eu-west-2.amazonaws.com/levavour/media/%s" width="100px" height="100px" />'%(self.logo))
    logo_tag.short_description = 'Logo Image'

    def second_banner_tag(self):
        return mark_safe('<img src="https://s3.eu-west-2.amazonaws.com/levavour/media/%s" width="150px" height="150px" />'%(self.second_banner))
    second_banner_tag.short_description = 'Second banner Image'

    def about_me_image_tag(self):
        return mark_safe('<img src="https://s3.eu-west-2.amazonaws.com/levavour/media/%s" width="100px" height="100px" />'%(self.about_me_image))
    about_me_image_tag.short_description = 'About me'

    def personal_photo_tag(self):
        return mark_safe('<img src="https://s3.eu-west-2.amazonaws.com/levavour/media/%s" width="100px" height="100px" />'%(self.personal_photo))
    personal_photo_tag.short_description = 'Personal_photo'

class MainBanner(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner/')
    header_message = models.CharField(max_length=100, default='George Avdoulos', help_text='Banner header message')
    text_message = models.TextField(help_text='Banner text message', default='Le Vavour Illustrator - Designer')
    color_text = models.CharField(max_length=10, default='#ffffff')
    font = models.CharField(max_length=200, default='http://fonts.googleapis.com/css?family=Roboto+Slab:400,700,100%7CRoboto:400,700,300,100')
    class Meta:
        verbose_name_plural = '2. Control the main banner'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="https://s3.eu-west-2.amazonaws.com/levavour/media/%s" width="300px" height="250px" />'%(self.image))
    image_tag.short_description = 'Image'
    def image_tag_tiny(self):
        return mark_safe('<img src="https://s3.eu-west-2.amazonaws.com/levavour/media/%s" width="150px" height="100px" />'%(self.image))
    image_tag.short_description = 'Image'

class AboutMe(models.Model):
    title = models.CharField(max_length=50, default='default')
    text = models.TextField(blank=True, help_text='Use HTML if you want!')
    class Meta:
        verbose_name_plural = '3. About Section'

    def __str__(self):
        return self.title


class AboutMeBar(models.Model):
    title = models.CharField(max_length=100,)
    percent = models.IntegerField(default=50, verbose_name='Number')
    icon = models.CharField(max_length=100,
                            null=True,
                            help_text='Here you use bootstrap icons, you can find them here. http://bootstrapmaster.com/live/one/icons_set2.html')
    class Meta:
        verbose_name_plural = 'The stats on front_page'
    def __str__(self):
        return self.title

class Services(models.Model):
    icon = models.CharField(max_length=100, null=True, help_text='Here you use bootstrap icons, you can find them here. http://bootstrapmaster.com/live/one/icons_set2.html')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=400, help_text='If you frontpage problems use <br> on end of line')
    order = models.IntegerField(default=1, help_text='Set the order if you want.')
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['order']
        verbose_name_plural = '4. Skill Set on front pages'
    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()
    day_added = models.DateField(auto_now=True)
    is_readed = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name

    def fullname(self):
        return '%s %s'%(self.first_name, self.last_name)

