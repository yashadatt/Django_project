# Generated by Django 4.2.9 on 2024-04-22 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='description',
        ),
        migrations.RemoveField(
            model_name='client',
            name='title',
        ),
    ]
