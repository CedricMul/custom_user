from django import forms
from user_app.models import MyUser

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["username", "displayname", "password"]

class SignInForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
