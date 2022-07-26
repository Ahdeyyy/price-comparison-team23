from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from price_compare.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    class Meta: 
        model = User
        fields= ('username','first_name','last_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

