from django.db import models

# User profile with basic details
class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    existing_diseases = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Symptoms can be associated with diseases (later if needed via ManyToMany)
class Symptom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Main disease model
class Disease(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='disease_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True) 
    symptoms = models.ManyToManyField(Symptom, related_name='diseases')

    age_group = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    causes = models.TextField(blank=True)
    prevention = models.TextField(blank=True)
    treatment = models.TextField(blank=True)  # ✅ Added treatment field here

    severity_level = models.CharField(
        max_length=20,
        choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe')],
        default='Mild'
    )
    is_chronic = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Medicine model linked to diseases
class Medicine(models.Model):
    MEDICINE_FORM_CHOICES = [
        ('Tablet', 'Tablet'),
        ('Syrup', 'Syrup'),
        ('Injection', 'Injection'),
        ('Ointment', 'Ointment'),
        ('Drops', 'Drops'),
    ]

    AGE_GROUP_CHOICES = [
        ('Infant', 'Infant'),
        ('Child', 'Child'),
        ('Adult', 'Adult'),
        ('Elderly', 'Elderly'),
    ]

    name = models.CharField(max_length=100)
    form = models.CharField(max_length=20, choices=MEDICINE_FORM_CHOICES)
    for_diseases = models.ManyToManyField(Disease, related_name="medicines")
    dosage = models.TextField()
    age_group = models.CharField(max_length=50, choices=AGE_GROUP_CHOICES)
    side_effects = models.TextField(blank=True)
    allergies_warning = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.age_group})"


# Hospital model
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    available_ambulance = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Appointment booking model
class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name} - {self.hospital.name} ({self.date.date()})"
