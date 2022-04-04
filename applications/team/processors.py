from .models import MemberTeam


def team_dict(request):
    members = MemberTeam.objects.all()
    team_info = {'team_dictionary': members}
    return team_info