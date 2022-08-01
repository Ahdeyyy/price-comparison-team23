# Generated by Django 4.0.6 on 2022-08-01 15:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('price_compare', '0009_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]