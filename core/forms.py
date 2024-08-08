from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm (UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': 'Enter your name...',
        'class': 'w-full px-6 py-4 rounded-xl'             
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs= {
        'placeholder': 'Enter your email...',
        'class': 'w-full px-6 py-4 rounded-xl'             
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'placeholder': 'Enter your password...',
        'class': 'w-full px-6 py-4 rounded-xl'             
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'placeholder': 'Repeat password...',
        'class': 'w-full px-6 py-4 rounded-xl'             
    }))