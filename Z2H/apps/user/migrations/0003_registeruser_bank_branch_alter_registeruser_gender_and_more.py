# Generated by Django 4.2.10 on 2024-03-16 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_z2huser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='bank_branch',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=64),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='marital_status',
            field=models.CharField(choices=[('single', 'single'), ('married', 'married')], max_length=64),
        ),
    ]
