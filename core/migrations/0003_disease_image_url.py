# Generated by Django 5.1.4 on 2025-05-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_medicine_for_disease_medicine_for_diseases"),
    ]

    operations = [
        migrations.AddField(
            model_name="disease",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
