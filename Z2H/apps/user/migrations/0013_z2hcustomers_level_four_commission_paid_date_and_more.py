# Generated by Django 5.0.6 on 2024-06-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_registeruser_is_admin_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='z2hcustomers',
            name='level_four_commission_paid_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='z2hcustomers',
            name='level_one_commission_paid_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='z2hcustomers',
            name='level_three_commission_paid_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='z2hcustomers',
            name='level_two_commission_paid_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
