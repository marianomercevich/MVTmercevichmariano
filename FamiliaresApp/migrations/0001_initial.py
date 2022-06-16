# Generated by Django 4.0.5 on 2022-06-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Apellido', models.CharField(max_length=40)),
                ('fecha_de_nacimento', models.DateField(blank=True, null=True)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
