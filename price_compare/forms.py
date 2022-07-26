from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('username','body')




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User
        fields= ('username','first_name','last_name','email','Password')