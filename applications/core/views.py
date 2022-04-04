from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def blog(request):
    return render(request, 'core/blog.html')


def contact(request):
    return render(request, 'core/contact.html')


def faq(request):
    return render(request, 'core/qa.html')


def us(request):
    return render(request, 'core/us.html')