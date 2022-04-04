from django.shortcuts import render
from .models import Faq, FaqVideo


# Create your views here.
def faq(request):
    faqs = Faq.objects.all()
    faqs_videos = FaqVideo.objects.all()
    return render(request, 'faq/qa.html', {
        'faqs': faqs, 
        'faqs_videos': faqs_videos,
    })