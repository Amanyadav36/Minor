from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q 
from django.http import JsonResponse
from .models import Disease, Medicine, Symptom
from .models import UserProfile 
from .forms import UserProfileForm

def signup_page(request):
    return render(request, 'core/signup.html')

def login_page(request):
    return render(request, 'core/login.html')

def profile_view(request):
    profile = UserProfile.objects.filter(email=request.user.email).first()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)  # Print errors if the form is invalid
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'core/profile.html', {'form': form, 'profile': profile})


def home(request):
    # Fetch 5 diseases for the home page
    diseases = Disease.objects.all()[:5]
    return render(request, 'core/home.html', {'diseases': diseases})

def search_results(request):
    query = request.GET.get('q', '').strip()
    diseases = []
    medicines = []

    if query:
        # Search for diseases by name or symptom
        diseases = Disease.objects.filter(
            Q(name__icontains=query) | Q(symptoms__name__icontains=query)
        ).distinct()

        # Search for medicines by name or linked disease name
        medicines = Medicine.objects.filter(
            Q(name__icontains=query) | Q(for_diseases__name__icontains=query)
        ).distinct()

        print("Query:", query)
        print("Diseases found:", diseases)
        print("Medicines found:", medicines)

    return render(request, 'core/search_results.html', {
        'query': query,
        'diseases': diseases,
        'medicines': medicines
    })

def save_user_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        name = f"{data.get('firstName', '')} {data.get('lastName', '')}"
        email = data.get('email')
        existing_diseases = data.get('existingDiseases', '')

        if UserProfile.objects.filter(email=email).exists():
            return JsonResponse({'error': 'User already exists'}, status=409)

        UserProfile.objects.create(
            name=name,
            email=email,
            password="",  # Don't store Firebase password
            existing_diseases=existing_diseases
        )
        return JsonResponse({'message': 'User profile saved successfully'}, status=201)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def all_conditions(request):
    # Fetch all diseases for the all conditions page
    diseases = Disease.objects.all()
    return render(request, 'core/all_conditions.html', {'diseases': diseases})
def disease_detail(request, disease_id):
    # Fetch the specific disease or return 404 if not found
    disease = get_object_or_404(Disease, id=disease_id)
    return render(request, 'core/disease_detail.html', {'disease': disease})
def autocomplete_search(request):
    query = request.GET.get('q', '').strip()
    suggestions = []

    if query:
        # Fetch diseases, symptoms, and medicines starting with the query (case-insensitive)
        diseases = Disease.objects.filter(name__istartswith=query)[:5]
        symptoms = Symptom.objects.filter(name__istartswith=query)[:5]
        medicines = Medicine.objects.filter(name__istartswith=query)[:5]

        # Combine suggestions with type and URL
        for disease in diseases:
            suggestions.append({
                'name': disease.name,
                'type': 'Disease',
                'url': f"/disease/{disease.id}/"
            })

        for symptom in symptoms:
            suggestions.append({
                'name': symptom.name,
                'type': 'Symptom',
                'url': '#'  # Placeholder; update if you have a symptom detail page
            })

        for medicine in medicines:
            suggestions.append({
                'name': medicine.name,
                'type': 'Medicine',
                'url': '#'  # Placeholder; update if you have a medicine detail page
            })

        # Sort by name and limit to 5 suggestions
        suggestions = sorted(suggestions, key=lambda x: x['name'].lower())[:5]

    return JsonResponse({'suggestions': suggestions})