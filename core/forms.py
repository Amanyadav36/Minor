from django import forms
from .models import UserProfile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'password', 'profile_pic', 'existing_diseases']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
class SearchForm(forms.Form):
    query = forms.CharField(label="Search by symptom or disease", max_length=100)
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'profile_pic', 'existing_diseases']
