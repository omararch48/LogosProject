from django.shortcuts import render
from .models import Testimonial


# Create your views here.
def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials/testimonials.html', {'testimonials': testimonials})