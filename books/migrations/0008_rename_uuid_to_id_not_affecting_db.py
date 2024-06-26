# Generated by Django 5.0.3 on 2024-04-12 09:36
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_delete_field_book_id'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.RenameField(
                    model_name='book',
                    old_name='uuid',
                    new_name='id',
                ),
                migrations.AlterField(
                    model_name='book',
                    name='id',
                    field=models.UUIDField(default=uuid.uuid4,
                          serialize=False, editable=False, primary_key=True),
                ),
            ],
        )
    ]
