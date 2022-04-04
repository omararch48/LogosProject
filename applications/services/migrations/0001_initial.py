# Generated by Django 4.0.3 on 2022-04-03 00:01

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Clasificación')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Clasificación',
                'verbose_name_plural': 'Clasificaciones',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre del servicio')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('name_english', models.CharField(blank=True, max_length=250, null=True, verbose_name='Service name')),
                ('description_english', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('order', models.SmallIntegerField(default=1, verbose_name='Orden')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('image', models.ImageField(blank=True, null=True, upload_to='servicess', verbose_name='Imagen')),
                ('active', models.CharField(choices=[('0', 'Activo'), ('1', 'Inactivo'), ('2', 'Descontinuado')], default='0', max_length=1, verbose_name='Estado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('classifications', models.ManyToManyField(to='services.classification', verbose_name='Clasificaciones')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['active', 'order', 'name'],
                'unique_together': {('name', 'description')},
            },
        ),
    ]
