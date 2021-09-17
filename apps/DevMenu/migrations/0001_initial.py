# Generated by Django 2.0.6 on 2021-09-04 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='platillos',
            fields=[
                ('pk_platillo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='restaurante',
            fields=[
                ('pk_restaurante', models.AutoField(primary_key=True, serialize=False)),
                ('dueño', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=70)),
            ],
        ),
    ]