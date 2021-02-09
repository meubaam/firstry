from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={ 'required': 'Title is required' }, max_length=128, label="title")
    contents = forms.CharField(
        error_messages={ 'required': 'Contents is required' },widget=forms.Textarea, label="contents")
    tags = forms.CharField(
        required = False, label ="#Tag"
    )
