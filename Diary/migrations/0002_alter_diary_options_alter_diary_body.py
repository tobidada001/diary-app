# Generated by Django 4.1 on 2024-04-04 12:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diary',
            options={'verbose_name_plural': 'Diaries'},
        ),
        migrations.AlterField(
            model_name='diary',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
