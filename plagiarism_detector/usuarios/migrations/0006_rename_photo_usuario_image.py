# Generated by Django 3.2 on 2021-05-10 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20210510_0228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='photo',
            new_name='image',
        ),
    ]