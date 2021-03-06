# Generated by Django 4.0.3 on 2022-04-03 00:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaqVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del vídeo')),
                ('video', models.FileField(upload_to='faq', verbose_name='Vídeo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'FAQ Vídeo',
                'verbose_name_plural': "FAQ's Videos",
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, verbose_name='Pregunta')),
                ('answer', ckeditor.fields.RichTextField(verbose_name='Respuesta')),
                ('question_english', models.CharField(blank=True, max_length=250, null=True, verbose_name='Question')),
                ('answer_english', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Answer')),
                ('order', models.SmallIntegerField(default=1, verbose_name='Orden')),
                ('active', models.CharField(choices=[('0', 'Activa'), ('1', 'Inactiva'), ('2', 'Descontinuada')], default='0', max_length=1, verbose_name='Estado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': "FAQ's",
                'ordering': ['active', 'order', '-created'],
                'unique_together': {('question', 'answer')},
            },
        ),
    ]
