from django.contrib import admin
from .models import *
from .forms import ImageFormSet
# Register your models here.

class ImageInline(admin.TabularInline):
    model = ImageProject
    fields = ['image_tag_tiny', 'image', 'title', 'alt', 'text', ]
    readonly_fields = ['image_tag_tiny']
    extra = 3

class SkillsInline(admin.TabularInline):
    model = SkillProgress
    extra = 2

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['image_tag_tiny', 'title','short_description', 'active']
    list_filter = ['active',]
    readonly_fields = ['image_tag','background_image_tag']
    inlines = [ImageInline, SkillsInline]
    fieldsets = (
        ('Homepage Info',{
            'fields':(('title', 'short_description'),('image_tag', 'image'),'active')
        }),
        ('Page Info',{
            'fields':(('description',   'category'),)
        }),
        ('Seo',{'classes': ('collapse',),
            'fields': ('seo_title', 'seo_keywords', 'seo_description', 'slug'),
        }),
        ('CSS Styling',{'classes': ('collapse',),
            'fields': ('css_background_color_menu', 'css_background_color', 'css_font_color', 'href_color', 'css_font_style',('background_image_tag','image_background_page')),
        }),
        ('About',{
            'fields': ('about_text','extra_info'),
        }),


    )

class ImageProjectAdmin(admin.ModelAdmin):
    list_display = ['image_tag_tiny', 'project_related','active','title']
    list_filter = ['project_related', 'active']
    readonly_fields = ('image_tag',)
    fields = ['active', 'project_related','image_tag','image','title', 'alt','text' ]




class SkillBarAdmin(admin.ModelAdmin):
    list_filter = ['project_related']

admin.site.register(Projects, ProjectAdmin)
admin.site.register(ImageProject, ImageProjectAdmin)
admin.site.register(SkillProgress, SkillBarAdmin)
admin.site.register(ProjectCategory)
