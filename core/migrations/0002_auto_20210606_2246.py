# Generated by Django 3.2.3 on 2021-06-07 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Usuario')),
                ('nombre', models.CharField(max_length=60, verbose_name='Primer nombre')),
                ('apellido', models.CharField(max_length=60, verbose_name='Primer apellido')),
                ('correo', models.CharField(max_length=60, verbose_name='correo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]
