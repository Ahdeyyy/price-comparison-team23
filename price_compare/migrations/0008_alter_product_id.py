# Generated by Django 4.0.6 on 2022-07-27 17:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('price_compare', '0007_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('87851dba-4ee5-4f50-b790-699bad679d10'), primary_key=True, serialize=False, unique=True),
        ),
    ]
