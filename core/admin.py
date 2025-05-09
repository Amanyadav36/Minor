from django.contrib import admin
from .models import UserProfile, Symptom, Disease, Medicine, Hospital, Appointment

admin.site.register(UserProfile)
admin.site.register(Symptom)
admin.site.register(Disease)
admin.site.register(Medicine)
admin.site.register(Hospital)
admin.site.register(Appointment)
