# Generated by Django 4.2.10 on 2024-05-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_z2horders_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='z2horders',
            name='order_number',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
