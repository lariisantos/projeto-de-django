# Generated by Django 5.0.6 on 2024-06-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_cantor_album_cantor'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='ano_lancamento',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='musica',
            name='duracao',
            field=models.CharField(max_length=5),
        ),
    ]
