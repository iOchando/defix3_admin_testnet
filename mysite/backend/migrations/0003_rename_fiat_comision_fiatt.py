# Generated by Django 4.0.4 on 2022-07-13 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_comision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comision',
            old_name='fiat',
            new_name='fiatt',
        ),
    ]
