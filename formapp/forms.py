from django import forms
from .models import Snippet

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField( label = 'Email')
    message = forms.CharField(widget=forms.Textarea)
    number = forms.IntegerField()


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name', 'body')