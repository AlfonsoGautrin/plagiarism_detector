# Generated by Django 3.1.5 on 2021-05-15 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essays', '0005_essay_task_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='essayplagiarism',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
