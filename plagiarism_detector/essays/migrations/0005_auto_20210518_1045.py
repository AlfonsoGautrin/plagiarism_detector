# Generated by Django 3.2 on 2021-05-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essays', '0004_alter_essay_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='essayplagiarism',
            name='date',
            field=models.DateTimeField(),
        ),
    ]