from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Projects, ImageProject
from homepage.models import Welcome_page
from django.template.defaultfilters import slugify

@receiver(post_save, sender = Projects)
def create_slug_and_seo(sender, instance, *args, **kwargs):
    title = slugify(instance.title)
    if not instance.seo_title:
        instance.seo_title = '%s'%(instance.title)
        instance.save()
    if not instance.slug:
        checks = Projects.objects.filter(slug=title)
        if checks:
            instance.slug = '%s-%s' %(title, checks.last().id)
            instance.save()
        else:
            instance.slug = title
            instance.save()
post_save.connect(create_slug_and_seo, sender=Projects)

@receiver(post_save, sender = ImageProject)
def create_title(sender, instance, *args, **kwargs):
    if not instance.title:
        instance.title = '%s'%(instance.project_related)
        instance.save()
    if not instance.alt:
        instance.alt = '%s'%(instance.project_related)
        instance.save()
post_save.connect(create_title, sender=ImageProject)