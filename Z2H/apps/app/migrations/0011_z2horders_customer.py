# Generated by Django 4.2.10 on 2024-05-27 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_registeruser_marital_status'),
        ('app', '0010_z2horders_courier_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='z2horders',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.z2hcustomers'),
        ),
    ]
