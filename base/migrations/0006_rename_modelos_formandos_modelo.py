# Generated by Django 4.0.6 on 2022-07-20 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_formandos_modelos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formandos',
            old_name='modelos',
            new_name='modelo',
        ),
    ]