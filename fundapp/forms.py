from django import forms
from .models import Contribution

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['name', 'amount']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Contributor Name'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount (TZS)'}),
        }
