from django.shortcuts import render, get_object_or_404
from .models import UsText


# Create your views here.
def us(request):
    us_texts = UsText.objects.all()
    return render(request, 'us/us.html', {'us_texts': us_texts})


def text(request, text_id):
    text = get_object_or_404(UsText, id=text_id)
    return render(request, 'us/text.html', {'text': text})
