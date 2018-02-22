from django.contrib import admin
from .models import *
# Register your models here.

def mass_active(modeladmin , request, queryset):
    for ele in queryset:
        if ele.active==False:
            ele.active = True

        else:
            ele.active = False
        ele.save()
mass_active.short_description= 'Mass active/deactive'


class ImageInline(admin.TabularInline):
    model = ImageArt
    extra = 3
    fields = ['image_tag_tiny', 'image', 'title', 'alt']
    readonly_fields = ['image_tag_tiny']

class ArtImageAdmin(admin.ModelAdmin):
    list_display = ['image_tag_tiny', 'project_related','active','title']
    list_filter = ['project_related', 'active']
    fields = ['active', 'project_related','image_tag','image','title', 'alt', ]
    readonly_fields = ['image_tag',]
    actions = [mass_active,]

class ArtAdmin(admin.ModelAdmin):
    list_display = ['image_tag_tiny', 'title','short_description', 'active']
    list_filter = ['active']
    readonly_fields = ['image_tag','background_image_tag']
    inlines = [ImageInline]
    actions = [mass_active,]
    fieldsets = (
        ('Homepage Info',{
            'fields':(('title', 'short_description'),('image_tag', 'image'), 'active')
        }),
        ('Page Info',{
            'fields':(('description',))
        }),
        ('Seo',{'classes': ('collapse',),
            'fields': ('seo_title', 'seo_keywords', 'seo_description', 'slug'),
        }),
        ('CSS Styling',{'classes': ('collapse',),
            'fields': ('css_background_color_menu', 'css_background_color', 'href_color', 'css_font_color', 'css_font_style',('background_image_tag','image_background_page')),
        }),
    )



admin.site.register(Art, ArtAdmin)
admin.site.register(ImageArt, ArtImageAdmin)
