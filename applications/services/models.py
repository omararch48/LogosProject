from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Categoría')
    name_english = models.CharField(max_length=250, verbose_name='Category', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    STATUS_CHOICE = (
        ('0', 'Activo',),        
        ('1', 'Inactivo',),        
        ('2', 'Descontinuado',),        
    )
    name = models.CharField(max_length=250, verbose_name='Servicio')
    description = RichTextField(verbose_name='Descripción')
    name_english = models.CharField(max_length=250, verbose_name='Service', null=True, blank=True)
    description_english = RichTextField(verbose_name='Description', null=True, blank=True)
    order = models.SmallIntegerField(verbose_name='Orden', default=1)
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='servicess', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    active = models.CharField(max_length=1, verbose_name='Estado', choices=STATUS_CHOICE, default='0')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') 
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['active', 'order', 'name',]
        unique_together = ('name', 'category',)

    def __str__(self) -> str:
        return self.name
        