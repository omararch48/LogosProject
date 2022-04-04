from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class UsText(models.Model):
    STATUS_CHOICE = (
        ('0', 'Activo',),        
        ('1', 'Inactivo',),        
        ('2', 'Descontinuado',),        
    )
    text_name = models.CharField(max_length=200, verbose_name='Nombre del texto')
    text = RichTextField(verbose_name='Texto')
    text_name_english = models.CharField(max_length=200, verbose_name='Text name', null=True, blank=True)
    text_english = RichTextField(verbose_name='Text', null=True, blank=True)
    video = models.FileField(verbose_name='Vídeo', upload_to='us', null=True, blank=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='us', null=True, blank=True)
    order = models.SmallIntegerField(verbose_name='Orden', default=1)
    active = models.CharField(max_length=1, verbose_name='Estado', choices=STATUS_CHOICE, default='0')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Texto (nosotros)'
        verbose_name_plural = 'Textos (nosotros)'
        ordering = ['active', 'order', 'text_name']

    def __str__(self) -> str:
        return self.text_name
