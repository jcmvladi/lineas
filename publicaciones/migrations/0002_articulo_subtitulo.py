# Generated by Django 2.1.3 on 2018-11-12 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='subtitulo',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
