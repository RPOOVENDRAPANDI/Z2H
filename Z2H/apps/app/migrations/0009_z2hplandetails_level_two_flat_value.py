# Generated by Django 4.2.10 on 2024-05-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_z2hplandetails_level_four_flat_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='z2hplandetails',
            name='level_two_flat_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
    ]
