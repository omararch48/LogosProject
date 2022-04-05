# Generated by Django 4.0.3 on 2022-04-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hometext',
            options={'ordering': ['active', 'order', 'name'], 'verbose_name': 'Texto (inicio)', 'verbose_name_plural': 'Textos (inicio)'},
        ),
        migrations.AddField(
            model_name='hometext',
            name='url_text',
            field=models.CharField(blank=True, default='Ver más', max_length=50, null=True, verbose_name='Texto del botón'),
        ),
        migrations.AddField(
            model_name='hometext',
            name='url_text_english',
            field=models.CharField(blank=True, default='Ver más', max_length=50, null=True, verbose_name='Button text'),
        ),
    ]