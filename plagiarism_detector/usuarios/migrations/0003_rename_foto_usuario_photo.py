# Generated by Django 3.2 on 2021-05-06 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20210506_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='foto',
            new_name='photo',
        ),
    ]