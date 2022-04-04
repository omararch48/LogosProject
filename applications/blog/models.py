from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Categoría')
    name_english = models.CharField(max_length=200, verbose_name='Category', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    STATUS_CHOICE = (
        ('0', 'Activo',),        
        ('1', 'Inactivo',),        
        ('2', 'Descontinuado',),        
    )
    title = models.CharField(max_length=200, verbose_name='Nombre')
    content = RichTextField(verbose_name='Contenido')
    title_english = models.CharField(max_length=200, verbose_name='Nombre', null=True, blank=True)
    content_english = RichTextField(verbose_name='Content', null=True, blank=True)
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    active = models.CharField(max_length=1, verbose_name='Estado', choices=STATUS_CHOICE, default='0')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['active', '-created']

    def __str__(self) -> str:
        return self.title
