# Generated by Django 3.2.18 on 2023-03-16 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20230316_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendedimage',
            name='image_path',
        ),
    ]
