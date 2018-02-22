from django.forms import formset_factory
from .models import *

ImageFormSet = formset_factory(ImageProject, extra=5)
