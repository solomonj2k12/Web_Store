from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class userloginform(forms.Form):
    ''' form to login in users to their accounts '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class userregisterform(UserCreationForm):
    '''this is a form to create new user '''
    password1 = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput)
        
    password2 = forms.CharField(
        label="Password Confirmation", 
        widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']