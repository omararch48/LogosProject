from .models import HomeText


def home_dict(request):
    home_texts = HomeText.objects.filter(active='0')
    home_info = {'home_texts': home_texts}
    return home_info