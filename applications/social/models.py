from pyexpat import model
from django.db import models


# Create your models here.
class Link(models.Model):
    SOCIAL_CHOICE = (
        ('fa-facebook', 'Facebook',),
        ('fa-instagram', 'Instagram',),
        ('fa-whatsapp', 'WhatsApp',),
        ('fa-telegram', 'Telegram',),
        ('fa-tiktok', 'Tiktok',),
        ('fa-youtube', 'YouTube',),
        ('fa-twitter', 'Twitter',),
        ('fa-linkedin   ', 'LinKedIn',),
    )
    STATUS_CHOICE = (
        ('0', 'Activa',),        
        ('1', 'Inactiva',),        
        ('2', 'Descontinuada',),        
    )
    key = models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='Red social', max_length=100, choices=SOCIAL_CHOICE)
    url = models.URLField(verbose_name='Enlace', max_length=250, null=True, blank=True)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)    
    description_english = models.TextField(verbose_name='Description', null=True, blank=True)
    order = models.SmallIntegerField(verbose_name='Orden', default=1)
    active = models.CharField(max_length=1, verbose_name='Estado', choices=STATUS_CHOICE, default='0')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
        
    class Meta:
        verbose_name = 'Red social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['active', 'order', 'name',]
        unique_together = ('key', 'name', 'url',)

    def __str__(self) -> str:
        return self.name