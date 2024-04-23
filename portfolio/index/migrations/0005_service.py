# Generated by Django 4.2.9 on 2024-04-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_remove_client_description_remove_client_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='services/')),
            ],
        ),
    ]