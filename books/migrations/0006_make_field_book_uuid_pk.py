# Generated by Django 5.0.3 on 2024-04-12 07:43
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_field_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uuid',
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False
            ),
        )
    ]
