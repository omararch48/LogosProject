# Generated by Django 4.0.3 on 2022-04-03 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Nombre clave')),
                ('name', models.CharField(choices=[('fa-facebook', 'Facebook'), ('fa-instagram', 'Instagram'), ('fa-whatsapp', 'WhatsApp'), ('fa-telegram', 'Telegram'), ('fa-tiktok', 'Tiktok'), ('fa-youtube', 'YouTube'), ('fa-twitter', 'Twitter'), ('fa-linkedin   ', 'LinKedIn')], max_length=100, verbose_name='Red social')),
                ('url', models.URLField(blank=True, max_length=250, null=True, verbose_name='Enlace')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('description_english', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('order', models.SmallIntegerField(default=1, verbose_name='Orden')),
                ('active', models.CharField(choices=[('0', 'Activa'), ('1', 'Inactiva'), ('2', 'Descontinuada')], default='0', max_length=1, verbose_name='Estado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Red social',
                'verbose_name_plural': 'Redes Sociales',
                'ordering': ['active', 'order', 'name'],
                'unique_together': {('key', 'name', 'url')},
            },
        ),
    ]
