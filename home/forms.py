from django.forms import ModelForm, TextInput, EmailInput, Textarea
from home.models import AloqaModel


class AloqaForm(ModelForm):
    class Meta:
        model = AloqaModel
        fields = ['name', 'subject', 'phone', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'Mavzu'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Sizning xabaringiz'}),
        }
