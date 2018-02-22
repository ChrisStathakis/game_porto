from django.contrib import admin
from .models import Contact
# Register your models here.

def mass_readed(modeladmin, request, queryset):
    for ele in queryset:
        ele.is_readed = True
        ele.save()
mass_readed.short_description ='Readed'


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email','date','first_name', 'last_name', 'is_readed']
    fields = ['is_readed','date', 'email', 'first_name', 'last_name','message','phone' ]
    list_filter = ['is_readed']
    readonly_fields = ['date','message', 'phone' ]
    actions = [mass_readed,]
admin.site.register(Contact, ContactAdmin)