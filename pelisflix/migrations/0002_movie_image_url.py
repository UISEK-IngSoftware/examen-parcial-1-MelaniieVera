# Generated by Django 4.2 on 2025-06-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelisflix', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image_url',
            field=models.URLField(blank=True, help_text='URL de la imagen de la película', null=True),
        ),
    ]
