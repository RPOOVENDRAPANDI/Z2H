# Generated by Django 4.2.10 on 2024-03-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='z2hplandetails',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
