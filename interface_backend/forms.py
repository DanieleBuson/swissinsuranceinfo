from django import forms
from .models import Faq

class GenerateFAQForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Faq
        fields = ["question"]