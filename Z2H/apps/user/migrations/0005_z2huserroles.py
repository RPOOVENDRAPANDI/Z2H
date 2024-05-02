# Generated by Django 4.2.10 on 2024-04-29 17:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_z2hcustomers_plan_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Z2HUserRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_uid', models.CharField(max_length=64)),
                ('role_uid', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]