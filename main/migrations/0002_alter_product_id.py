# Generated by Django 5.1 on 2024-09-17 17:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
