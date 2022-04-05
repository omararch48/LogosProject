# Generated by Django 4.0.3 on 2022-04-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_hometext_options_hometext_url_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometext',
            name='image_one',
            field=models.CharField(max_length=255, verbose_name='URL Imagen 2'),
        ),
        migrations.AlterField(
            model_name='hometext',
            name='image_two',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL Imagen 2 (solo para mosaico)'),
        ),
        migrations.AlterField(
            model_name='hometext',
            name='url_text_english',
            field=models.CharField(blank=True, default='More', max_length=50, null=True, verbose_name='Button text'),
        ),
    ]
