from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class MemberTeam(models.Model):
    STATUS_CHOICE = (
        ('0', 'Activo',),        
        ('1', 'Inactivo',),        
        ('2', 'Descontinuado',),        
    )
    member = models.ForeignKey(User, verbose_name='Integrante', on_delete=models.CASCADE)
    position = models.CharField(max_length=200, verbose_name='Cargo')
    position_english = models.CharField(max_length=200, verbose_name='Position', null=True, blank=True)
    photo = models.ImageField(verbose_name='Foto (opcional)', upload_to='team', null=True, blank=True)
    bio = RichTextField(verbose_name='Biografía', null=True, blank=True)
    bio_english = RichTextField(verbose_name='Biography', null=True, blank=True)
    active = models.CharField(max_length=1, verbose_name='Estado', choices=STATUS_CHOICE, default='0')

    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'
        ordering = ['active', 'member']

    def __str__(self) -> str:
        return str(self.member)
