from django import forms
from .models import Review

class SearchForm(forms.Form):
    searchWord = forms.CharField(max_length = 200, label="", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Search GameBean'}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'username'}))
    password = forms.CharField(max_length = 15, widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder':'password'}))


class ReviewForm(forms.Form):
    title = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Write Topic of reiview here'}))
    text = forms.CharField(max_length = 200, widget=forms.Textarea(attrs={'class' : 'form-control', 'style' : 'height:100px', 'placeholder' : 'Write you\'re review here'}))
    class Meta:
        model = Review
        
class SignUpForm(forms.Form):
    email = forms.CharField(max_length = 200,  widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'email'}))
    username = forms.CharField(max_length = 200,  widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'username'}))
    password = forms.CharField(max_length = 15,  widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder':'password'}))
    confirmation_password = forms.CharField(max_length = 15,  widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder':'confirm password'}))

class ProfileImageForm(forms.Form):
    image= forms.ImageField(label="Change profile image")
