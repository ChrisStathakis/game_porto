"""vavouras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from homepage.views import *
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from site_map.views import *
from django.views.generic import TemplateView


sitemaps = {
    'art':ArtSitemap,
    'project':ProjectSitemap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Homepage.as_view(), name='home'),
    url(r'^about/$', AboutPage.as_view(), name='about'),
    url(r'^art/$', ArtPage.as_view(), name='art'),
    url(r'^art/(?P<slug>[-\w]+)/$', view=choosed_art, name='choosed_art'),
    url(r'^projects/$', ProjectsPage.as_view(), name='projects'),
    url(r'^project/(?P<slug>[-\w]+)/$', view=project, name='project'),
    url(r'^project/image/(?P<dk>\d+)/$', view=project_image, name='project_image'),
    url(r'^project-about/(?P<slug>[-\w]+)/$', view=project_about, name='project_about'),
    url(r'^message$', view=message_success, name='message'),
    url(r'^sitemap\.xml',sitemap, {'sitemaps': sitemaps}),
    url(r'^robots.txt$', TemplateView.as_view(template_name="it_worker/robots.txt", content_type="text/plain"), name="robots_file")

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)