# Generated by Django 4.0.4 on 2022-07-13 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_comision_comisions_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comisions',
            new_name='Comision',
        ),
    ]