from django.contrib import admin
from .models import Testimonial


# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('testimonial', 'active',)
    search_fields = ('testimonial', 'active',)


admin.site.register(Testimonial, TestimonialAdmin)