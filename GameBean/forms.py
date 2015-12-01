from django import forms

class SearchForm(forms.Form):
    searchWord = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Search GameBean'}))


class ReviewForm(forms.Form):
    topic = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Write Topic of reiview here'}))
    text = forms.CharField(max_length = 200, widget=forms.Textarea(attrs={'class' : 'form-control', 'style' : 'height:100px', 'placeholder' : 'Write you\'re review here'}))
