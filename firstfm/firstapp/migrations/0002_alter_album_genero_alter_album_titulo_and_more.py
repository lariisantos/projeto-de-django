# Generated by Django 5.0.6 on 2024-06-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genero',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='album',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='musica',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
