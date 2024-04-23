# Generated by Django 4.2.9 on 2024-04-23 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=1000)),
                ('email', models.EmailField(max_length=100)),
                ('mobile_number', models.IntegerField(max_length=10)),
            ],
        ),
    ]
