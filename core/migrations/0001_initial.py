# Generated by Django 5.2 on 2025-04-14 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='disease_images/')),
                ('age_group', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('causes', models.TextField(blank=True)),
                ('prevention', models.TextField(blank=True)),
                ('treatment', models.TextField(blank=True)),
                ('severity_level', models.CharField(choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe')], default='Mild', max_length=20)),
                ('is_chronic', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
                ('specialization', models.CharField(max_length=100)),
                ('available_ambulance', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('existing_diseases', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('form', models.CharField(choices=[('Tablet', 'Tablet'), ('Syrup', 'Syrup'), ('Injection', 'Injection'), ('Ointment', 'Ointment'), ('Drops', 'Drops')], max_length=20)),
                ('dosage', models.TextField()),
                ('age_group', models.CharField(choices=[('Infant', 'Infant'), ('Child', 'Child'), ('Adult', 'Adult'), ('Elderly', 'Elderly')], max_length=50)),
                ('side_effects', models.TextField(blank=True)),
                ('allergies_warning', models.TextField(blank=True)),
                ('for_disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disease')),
            ],
        ),
        migrations.AddField(
            model_name='disease',
            name='symptoms',
            field=models.ManyToManyField(related_name='diseases', to='core.symptom'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('is_confirmed', models.BooleanField(default=False)),
                ('disease', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.disease')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hospital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userprofile')),
            ],
        ),
    ]
