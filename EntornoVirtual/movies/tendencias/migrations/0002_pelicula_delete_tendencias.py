# Generated by Django 5.0.7 on 2024-07-19 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='imagen')),
                ('datos', models.TextField()),
                ('director', models.TextField()),
                ('director2', models.TextField()),
                ('escritor', models.TextField()),
            ],
            options={
                'verbose_name': 'Pelicula',
                'verbose_name_plural': 'Peliculas',
            },
        ),
        migrations.DeleteModel(
            name='tendencias',
        ),
    ]
