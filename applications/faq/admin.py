from django.contrib import admin
from .models import Faq, FaqVideo


# Register your models here.
class FaqAdminVideo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('name',)


class FaqAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('question', 'order',)
    list_filter = ('question', 'question_english',)


admin.site.register(Faq, FaqAdmin)
admin.site.register(FaqVideo, FaqAdminVideo)