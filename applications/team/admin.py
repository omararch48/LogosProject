from django.contrib import admin
from .models import MemberTeam


# Register your models here.
class MemberTeamAdmin(admin.ModelAdmin):
    list_display = ('member', 'position', 'active',)
    list_filter = ('active',)

admin.site.register(MemberTeam, MemberTeamAdmin)