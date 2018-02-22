from projects.models import *


def projects_filters(request, queryset):

    search_name = request.GET.get('search_name')
    cate_name = request.GET.getlist('cate_name')
    try:
        queryset = queryset.filter(category__id__in=cate_name) if cate_name else queryset
    except:
        queryset = queryset
    queryset = queryset.filter(title__icontains=search_name) if search_name else queryset
    return [search_name, cate_name, queryset]
