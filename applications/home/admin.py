from django.contrib import admin
from .models import HomeText


# Register your models here.
class HomeTextAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'active',)
    readonly_fields = ('created', 'updated',)


admin.site.register(HomeText, HomeTextAdmin)