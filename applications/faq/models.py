from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class FaqVideo(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del vídeo')
    video = models.FileField(verbose_name='Vídeo', upload_to='faq')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') 
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'FAQ Vídeo'
        verbose_name_plural = 'FAQ\'s Videos'
        ordering = ['name',]

    def __str__(self) -> str:
        return self.name


class Faq(models.Model):
    STATUS_CHOICE = (
        ('0', 'Activa',),        
        ('1', 'Inactiva',),        
        ('2', 'Descontinuada',),        
    )
    question = models.CharField(max_length=250, verbose_name='Pregunta')
    answer = RichTextField(verbose_name='Respuesta')
    question_english = models.CharField(max_length=250, verbose_name='Question', null=True, blank=True)
    answer_english = RichTextField(verbose_name='Answer', null=True, blank=True)
    order = models.SmallIntegerField(verbose_name='Orden', default=1)
    active = models.CharField(max_length=1, verbose_name='Estado', choices=STATUS_CHOICE, default='0')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') 
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ\'s'
        ordering = ['active', 'order', '-created',]
        unique_together = ('question', 'answer',)

    def __str__(self) -> str:
        return self.question
        