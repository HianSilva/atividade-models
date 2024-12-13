# Generated by Django 5.1.4 on 2024-12-12 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_produto_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ManyToManyField(related_name='categoria', to='products.categoria'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='fornecedor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fornecedor', to='products.fornecedor'),
        ),
    ]
