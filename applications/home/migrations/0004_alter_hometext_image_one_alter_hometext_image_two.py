# Generated by Django 4.0.3 on 2022-04-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_hometext_image_one_alter_hometext_image_two_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometext',
            name='image_one',
            field=models.URLField(max_length=255, verbose_name='URL Imagen 2'),
        ),
        migrations.AlterField(
            model_name='hometext',
            name='image_two',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='URL Imagen 2 (solo para mosaico)'),
        ),
    ]
