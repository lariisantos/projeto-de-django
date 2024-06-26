# Generated by Django 5.0.6 on 2024-06-27 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_alter_album_genero_alter_album_titulo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cantor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='cantor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.cantor'),
        ),
    ]
