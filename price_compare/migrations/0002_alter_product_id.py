# Generated by Django 4.0.6 on 2022-07-26 13:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('price_compare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('04b78ca1-2d1b-436e-81bf-28b01d236ad3'), primary_key=True, serialize=False, unique=True),
        ),
    ]
