from django.db import models


# Create your models here.
class Testimonial(models.Model):
    STATUS_CHOICE = (
        ('0', 'Activo',),        
        ('1', 'Inactivo',),        
        ('2', 'Descontinuado',),        
    )
    testimonial = models.CharField(max_length=200, verbose_name='Testimoio(s)')
    testimonial_msg = models.TextField(verbose_name='Mensaje (opcional)', null=True, blank=True)
    testimonial_msg_english = models.TextField(verbose_name='Message (optional)', null=True, blank=True)
    video = models.FileField(verbose_name='Vídeo', upload_to='testimonials')
    active = models.CharField(max_length=1, verbose_name='Estado', choices=STATUS_CHOICE, default='0')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
        ordering = ['active', '-created',]

    def __str__(self) -> str:
        return self.testimonial