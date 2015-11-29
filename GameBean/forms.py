from django import forms

class SearchForm(forms.Form):
    searchWord = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Search GameBean'}))
