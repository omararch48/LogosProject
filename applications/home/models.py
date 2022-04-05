from django.db import models


# Create your models here.
class HomeText(models.Model):
    VIEW_CHOICE = (
        ('image-red', 'Componente imagen rojo',),
        ('image-green', 'Componente imagen verde',),
        ('image-green-two', 'Componente imagen verde claro',),
        ('mosaic', 'Mosaico',),
    )
    STATUS_CHOICE = (
        ('0', 'Activo',),        
        ('1', 'Inactivo',),        
        ('2', 'Descontinuado',),        
    )
    name = models.CharField(verbose_name='Texto inicio', max_length=200)
    model = models.CharField(
        max_length=30, 
        verbose_name='Modelo texto inicio', 
        choices=VIEW_CHOICE, 
        default='image-red'
    )
    description = models.TextField(verbose_name='Descripción')    
    description_english = models.TextField(
        verbose_name='Description', 
        null=True, 
        blank=True
    )    
    image_one = models.URLField(verbose_name='URL Imagen 2', max_length=255)
    image_two = models.URLField(
        verbose_name='URL Imagen 2 (solo para mosaico)', 
        max_length=255, 
        null=True, 
        blank=True
    )
    url_text = models.CharField(
        verbose_name='Texto del botón',
        max_length=50, 
        null=True, 
        blank=True,
        default='Ver más'
    )
    url_text_english = models.CharField(
        verbose_name='Button text',
        max_length=50, 
        null=True, 
        blank=True,
        default='More'
    )
    url = models.URLField(
        verbose_name='Enlace del texto', 
        max_length=250,
    )
    order = models.SmallIntegerField(verbose_name='Orden', default=1)
    active = models.CharField(
        max_length=1, 
        verbose_name='Estado', 
        choices=STATUS_CHOICE, 
        default='0'
    )
    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha de creación'
    )
    updated = models.DateTimeField(
        auto_now=True, 
        verbose_name='Fecha de edición'
    )
        
    class Meta:
        verbose_name = 'Texto (inicio)'
        verbose_name_plural = 'Textos (inicio)'
        ordering = ['active', 'order', 'name',]

    def __str__(self) -> str:
        return self.name