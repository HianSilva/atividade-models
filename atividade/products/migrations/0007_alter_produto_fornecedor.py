# Generated by Django 5.1.4 on 2024-12-13 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_produto_categoria_alter_produto_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fornecedor', to='products.fornecedor'),
        ),
    ]