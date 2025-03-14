from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','is_active','is_staff']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'})
    )

    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'})
    )




