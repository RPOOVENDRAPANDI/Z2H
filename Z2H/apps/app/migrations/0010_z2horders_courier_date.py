# Generated by Django 4.2.10 on 2024-05-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_z2hplandetails_level_two_flat_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='z2horders',
            name='courier_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
