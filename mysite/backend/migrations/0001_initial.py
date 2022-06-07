# Generated by Django 4.0.4 on 2022-06-07 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('mayor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='backend.modulo')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, help_text='esta el usuario activo?')),
                ('tipo', models.CharField(choices=[('S', 'Super'), ('A', 'Admin'), ('U', 'Usuario'), ('B', 'Banco')], default='U', help_text='Tipo de usuario', max_length=1, null=True)),
                ('usuario', models.OneToOneField(help_text='usuario asociado', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leer', models.BooleanField(default=False, help_text='Tiene opcion de leer?')),
                ('escribir', models.BooleanField(default=False, help_text='Tiene opcion de escribir?')),
                ('borrar', models.BooleanField(default=False, help_text='Tiene opcion de borrar?')),
                ('actualizar', models.BooleanField(default=False, help_text='Tiene opcion de actualizar?')),
                ('modulo', models.ForeignKey(help_text='Opcion de menu asociada', on_delete=django.db.models.deletion.CASCADE, to='backend.modulo')),
                ('perfil', models.ForeignKey(help_text='Usuario asociado', on_delete=django.db.models.deletion.CASCADE, to='backend.perfil')),
            ],
        ),
    ]