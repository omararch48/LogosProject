from django.contrib import admin
from .models import UsText


# Register your models here.
class UsTextAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('text_name', 'order',)
    search_fields = ('text_name', 'order', 'active',)


admin.site.register(UsText, UsTextAdmin)