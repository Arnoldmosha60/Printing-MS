# Generated by Django 4.0.7 on 2023-10-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_document_document_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
