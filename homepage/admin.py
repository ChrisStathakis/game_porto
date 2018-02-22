from django.contrib import admin
from .models import *
# Register your models here.



class WelcomePageAdmin(admin.ModelAdmin):
    readonly_fields = ['logo_tag','second_banner_tag', 'about_me_image_tag', 'personal_photo_tag']
    fieldsets = (
        (None, {
            'fields':('active', 'title')
        }),
        ('Photos', {
            'fields': (('logo_tag', 'logo'),
                       ('second_banner_tag', 'second_banner'),
                       ('about_me_image_tag','about_me_image'),
                       ('personal_photo_tag', 'personal_photo'))
        }),
        ('Text before footer', {
            'fields': (('left_text', 'center_text', 'right_text'))
        }),
        ('Site Config', {
            'fields': (('about_me',),
                       ('my_skills','my_skills_section_message'),
                       ('project', 'projects_section_message',),
                       'art_section_message', 'blog_section_message')

        }),

        ('Seo-Warning not need to change', {
            'classes': ('collapse',),
            'fields': ('seo_title', 'seo_keywords', 'seo_description'),
        }),
        ('CSS MODIFIER', {
            'fields': (('main_color_fonts','secondary_color_font','third_color_font'),('body_background_color', 'menu_hover_color'), ('skills_color_primary', 'skills_color_secondary'),),
        }),
    )

class BannerAdmin(admin.ModelAdmin):
    list_display = ['image_tag_tiny', 'title', 'active']
    list_filter = ['active']
    readonly_fields = ['image_tag']
    fields = ['active', 'title', 'alt', 'image_tag', 'image', 'header_message', 'text_message', 'color_text', 'font']




admin.site.register(Welcome_page, WelcomePageAdmin)
admin.site.register(MainBanner, BannerAdmin)
admin.site.register(Services)
admin.site.register(AboutMe)
#admin.site.register(AboutMeBar)
