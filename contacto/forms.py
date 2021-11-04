from django import forms

from webapp.models import Contacto

class FormularioContacto(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'email' : 'Email',
            'mensaje': 'Mensaje',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }


