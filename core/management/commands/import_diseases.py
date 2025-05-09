# myapp/management/commands/import_diseases.py
import json
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Disease, Symptom, Medicine

class Command(BaseCommand):
    help = 'Import diseases from JSON with nested symptoms and medicines'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['json_file']
        
        with open(file_path) as f:
            data = json.load(f)
            
            with transaction.atomic():
                for disease_data in data:
                    # Create Disease (same as before)
                    disease = Disease.objects.create(
                        name=disease_data['name'],
                        description=disease_data.get('description', ''),
                        causes=disease_data.get('causes', ''),
                        prevention=disease_data.get('prevention', ''),
                        treatment=disease_data.get('treatment', ''),
                        severity_level=disease_data.get('severity_level', 'Moderate'),
                        is_chronic=disease_data.get('is_chronic', False),
                        age_group=disease_data.get('age_group', 'Adult'),
                        image=None
                    )

                    # Process symptoms (same as before)
                    symptoms = []
                    for symptom_name in disease_data.get('symptoms', []):
                        symptom, _ = Symptom.objects.get_or_create(name=symptom_name)
                        symptoms.append(symptom)
                    disease.symptoms.set(symptoms)

                    # FIXED: Create medicines one-by-one
                    for med_data in disease_data.get('medicines', []):
                        medicine = Medicine.objects.create(
                            name=med_data['name'],
                            form=med_data.get('form', 'Tablet'),
                            dosage=med_data.get('dosage', ''),
                            age_group=med_data.get('age_group', 'Adult'),
                            side_effects=med_data.get('side_effects', ''),
                            allergies_warning=med_data.get('allergies_warning', '')
                        )
                        medicine.for_diseases.add(disease)  # Now has an ID

                self.stdout.write(
                    self.style.SUCCESS(f'Successfully imported {len(data)} diseases')
                )