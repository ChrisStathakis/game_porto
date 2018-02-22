from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Art, ImageArt
from homepage.models import Welcome_page
from django.template.defaultfilters import slugify


@receiver(post_save, sender = Art)
def create_slug_and_seo(sender, instance, *args, **kwargs):
    title = slugify(instance.title)
    site_title = Welcome_page.objects.get(id=1)
    if not instance.seo_title:
        instance.seo_title ='%s - %s'.strip()%(site_title.title, instance.title)
        instance.save()
    if not instance.slug:
        checks = Art.objects.filter(slug = title)
        if checks:
            print('works!')
            instance.slug = '%s-%s' %(title, checks.last().id)
            instance.save()
        else:
            instance.slug = title
            instance.save()
post_save.connect(create_slug_and_seo, sender=Art)

@receiver(post_save, sender = ImageArt)
def create_title(sender, instance, *args, **kwargs):
    if not instance.title:
        instance.title = '%s'%(instance.project_related)
        instance.save()
    if not instance.alt:
        instance.alt = '%s'%(instance.project_related)
        instance.save()

post_save.connect(create_title, sender=ImageArt)