# Generated by Django 4.0.4 on 2022-07-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('coin', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('blockchain', models.CharField(max_length=255)),
                ('transfer', models.FloatField()),
                ('swap', models.FloatField()),
                ('fiat', models.FloatField()),
            ],
        ),
    ]
