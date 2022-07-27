# Generated by Django 4.0.6 on 2022-07-27 15:00

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
            field=models.UUIDField(default=uuid.UUID('a1383fec-cbce-4329-b0a5-d1a1678aefcc'), primary_key=True, serialize=False, unique=True),
        ),
    ]