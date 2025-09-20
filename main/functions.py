from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random


def paginate_instances(request, instances, per_page=10, random_page=False):
    paginator = Paginator(instances, per_page)
    
    if random_page:
        page = request.GET.get("page", random.randint(1, paginator.num_pages))
    else:
        page = request.GET.get("page", 1)

    try:
        paginator_instances = paginator.page(page)
    except PageNotAnInteger:
        paginator_instances = paginator.page(1)
    except EmptyPage:
        paginator_instances = paginator.page(paginator.num_pages)
    
    next_page_number = None
    has_next_page = False
    if paginator_instances.has_next():
        has_next_page = True
        next_page_number = paginator_instances.next_page_number()

    previous_page_number = None
    has_previous_page = False
    if paginator_instances.has_previous():
        has_previous_page = True
        previous_page_number = paginator_instances.previous_page_number()
    
    paginator_response = {
        'current_page': paginator_instances.number,
        'has_next_page': has_next_page,
        'next_page_number': next_page_number,
        'has_previous_page': has_previous_page,
        'previous_page_number': previous_page_number,
        'total_pages': paginator.num_pages,
        'total_items': paginator.count,
    }
    
    return paginator_instances, paginator_response