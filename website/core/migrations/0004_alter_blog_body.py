# Generated by Django 5.1 on 2024-08-16 16:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
