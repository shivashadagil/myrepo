# Generated by Django 4.1.2 on 2023-02-07 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_add_files_img_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_files',
            name='img_number',
        ),
    ]
