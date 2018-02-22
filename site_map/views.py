from art.models import Art
from projects.models import Projects
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
import datetime



class ArtSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Art.objects.filter(active=True)

class ProjectSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Projects.objects.filter(active=True)


