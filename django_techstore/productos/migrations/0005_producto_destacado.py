# Generated by Django 5.2 on 2025-04-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_remove_producto_categoria_remove_producto_destacado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='destacado',
            field=models.BooleanField(default=False),
        ),
    ]
