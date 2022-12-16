from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['event_name', 'event_type', 'event_date',
                  'duration', 'venue', 'target_group']
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}, format='%d-%m-%Y'), 
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'target_group': forms.Select(attrs={'class': 'form-control'}),
        }
