from django.shortcuts import render
from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse,\
    redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import ListView, FormView, TemplateView
from .models import *
from .tools import projects_filters
from blog.models import Post, PostCategory
from art.models import Art, ImageArt
from projects.models import Projects, ImageProject, SkillProgress, ProjectCategory
from blog.views import *
from contact.forms import *
import datetime
# Create your views here.

'''
def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')


def language(request):
    lang = 'gr'
    response = HttpResponseRedirect('/')
    response.set_cookie('lang', lang)
    return response
'''


def initial_data(request):
    welcome_page = Welcome_page.objects.filter(active=True).last()
    banner = MainBanner.objects.filter(active=True).last()
    about = AboutMe.objects.get(id=1)
    arts = Art.my_query.active()
    return [welcome_page, banner, about]


class Homepage(FormView):
    template_name = 'it_worker/index.html'
    form_class = ContactForm
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        welcome_page, banner, about = initial_data(self.request)
        arts, projects = Art.my_query.active()[0:3], Projects.my_query.active()[0:3]
        context.update(locals())
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            send_mail('New Contact', '%s'%(form.cleaned_data.get('message')),
                      recipient_list=['lirageika@hotmail.gr'],
                      fail_silently=True,
                      from_email='%s' %(form.cleaned_data.get('email')))
            messages.success(self.request, 'I will contact you shortly!')
            return redirect('/')


class AboutPage(TemplateView):
    template_name = 'it_worker/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        welcome_page, banner, about = initial_data(self.request)
        context.update(locals())
        return context


def message_success(request):
    return render(request, 'it_worker/message.html')





class ProjectsPage(ListView):
    model = Projects
    template_name = 'it_worker/projects.html'

    def get_queryset(self):
        queryset = Projects.objects.all()
        search_name, cate_name, queryset = projects_filters(self.request, queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProjectsPage, self).get_context_data(**kwargs)
        welcome_page = Welcome_page.objects.last()
        categories = ProjectCategory.objects.all()
        search_name, cate_name, queryset = projects_filters(self.request, self.object_list)
        context.update(locals())
        return context


def project(request, slug):
    welcome_page = Welcome_page.objects.filter(active=True).last()
    project = get_object_or_404(Projects, slug=slug)
    images = ImageProject.my_query.post_related_and_active(post=project)
    context = locals()
    return render_to_response('creative/index.html', context)


class ArtPage(ListView):
    model = Art
    template_name = 'it_worker/art_page.html'

    def get_queryset(self):
        queryset = Art.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ArtPage, self).get_context_data(**kwargs)
        welcome_page = Welcome_page.objects.all().last()
        context.update(locals())
        return context


def choosed_art(request, slug):
    welcome_page = Welcome_page.objects.filter(active=True).last()
    project = get_object_or_404(Art, slug=slug)
    images = ImageArt.my_query.post_related_and_active(post=project)
    context = locals()
    return render_to_response('it_worker/art_details.html', context)


def project_image(request,dk):
    welcome_page = Welcome_page.objects.filter(active=True).last()
    image = get_object_or_404(ImageProject, id=dk)
    project = image.project_related
    context = locals()
    return render_to_response('creative/detail.html', context)


def project_about(request, slug):
    project = get_object_or_404(Projects, slug=slug)
    welcome_page = Welcome_page.objects.filter(active=True).last()
    skill_bar = SkillProgress.objects.filter(project_related = project)
    context = locals()
    return render_to_response('creative/about.html', context)