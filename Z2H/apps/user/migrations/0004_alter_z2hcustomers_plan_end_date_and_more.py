# Generated by Django 4.2.10 on 2024-04-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_z2huser_is_first_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='z2hcustomers',
            name='plan_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='z2hcustomers',
            name='plan_start_date',
            field=models.DateTimeField(),
        ),
    ]