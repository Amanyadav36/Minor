import json

# Load the JSON file
with open('diseases_data_300_cleaned.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Step 1: Deduplicate diseases (keep only the first one with each unique name)
unique_diseases = {}
for disease in data:
    disease_name = disease['name'].strip().lower()
    if disease_name not in unique_diseases:
        # Step 2: Deduplicate medicines inside this disease
        seen_meds = set()
        unique_meds = []
        for med in disease.get('medicines', []):
            key = (med['name'].strip().lower(), med['form'], med['dosage'])
            if key not in seen_meds:
                seen_meds.add(key)
                unique_meds.append(med)
        disease['medicines'] = unique_meds

        # Add the cleaned disease
        unique_diseases[disease_name] = disease

# Final cleaned list of diseases
cleaned_data = list(unique_diseases.values())

# Save to a new file
with open('diseases_data_300_cleaned2.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, indent=4)
