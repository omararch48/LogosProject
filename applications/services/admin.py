from django.contrib import admin
from .models import Service, Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('name', 'published', 'category', 'order',)
    search_fields = ('name', 'description', 'category',)
    date_hierarchy = 'published'
    list_filter = ('category',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)