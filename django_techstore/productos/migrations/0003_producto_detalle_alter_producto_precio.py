# Generated by Django 5.2 on 2025-04-16 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_destacado'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='detalle',
            field=models.TextField(default='Sin detalles'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]
