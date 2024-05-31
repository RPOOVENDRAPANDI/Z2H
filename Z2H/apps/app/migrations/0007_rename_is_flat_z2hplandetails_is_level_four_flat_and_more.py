# Generated by Django 4.2.10 on 2024-05-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_z2hplandetails_is_flat_z2hplandetails_is_percentage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='z2hplandetails',
            old_name='is_flat',
            new_name='is_level_four_flat',
        ),
        migrations.RenameField(
            model_name='z2hplandetails',
            old_name='is_percentage',
            new_name='is_level_four_percentage',
        ),
        migrations.RenameField(
            model_name='z2hplandetails',
            old_name='percentage_value',
            new_name='level_four_percentage_value',
        ),
        migrations.AddField(
            model_name='z2hplandetails',
            name='is_level_one_flat',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='z2hplandetails',
            name='is_level_one_percentage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='z2hplandetails',
            name='is_level_three_flat',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='z2hplandetails',
            name='is_level_three_percentage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='z2hplandetails',
            name='is_level_two_flat',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='z2hplandetails',
            name='is_level_two_percentage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='z2hplandetails',
            name='level_one_percentage_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
        migrations.AddField(
            model_name='z2hplandetails',
            name='level_three_percentage_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
        migrations.AddField(
            model_name='z2hplandetails',
            name='level_two_percentage_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
    ]