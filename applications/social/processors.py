from .models import Link


def social_dict(request):
    links = Link.objects.all()
    social_info = {'social_dictionary': links}
    return social_info