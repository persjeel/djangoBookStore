# Generated by Django 5.0.3 on 2024-04-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0004_auto_20240412_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(),
        )
    ]