# Generated by Django 3.2 on 2021-05-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_rename_photo_usuario_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='image',
            field=models.ImageField(upload_to='users_images'),
        ),
    ]
