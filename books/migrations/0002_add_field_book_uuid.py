# Generated by Django 5.0.3 on 2024-04-12 06:58

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, serialize=False, null=True),
        ),
    ]
