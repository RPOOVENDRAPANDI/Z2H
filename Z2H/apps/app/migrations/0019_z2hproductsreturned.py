# Generated by Django 5.0.6 on 2024-06-14 22:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_z2hproducts_product_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Z2HProductsReturned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('product_id', models.CharField(blank=True, max_length=64, null=True)),
                ('customer_id', models.CharField(blank=True, max_length=64, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('product_returned_date', models.DateTimeField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]