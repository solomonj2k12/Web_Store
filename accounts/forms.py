from django import forms


class userloginform(forms.Form):
    ''' form to login in users to their accounts '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)