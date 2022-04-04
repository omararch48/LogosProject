from django.shortcuts import render, get_object_or_404
from .models import Service, Category


# Create your views here.
def categories(request):
    categories = Category.objects.all()
    return render(request, 'services/categories.html', {'categories': categories})

def services(request, category_name):
    services_total = Service.objects.all()
    services = []
    for element in services_total:
        if element.category.name == category_name:
            services.append(element)
    return render(request, 'services/services.html', {
        'services': services,
        'category_name': category_name,
    })


def service(request, service_id, service_category):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'services/service.html', {
        'service': service,
        'service_category': service_category,
    })