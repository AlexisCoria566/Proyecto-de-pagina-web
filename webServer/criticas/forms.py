from django import forms

from criticas.models import Opinion


class OpinionForm(forms.ModelForm):

    class Meta:
        model = Opinion
        fields = ['nombre', 'comentario', 'imagen','calificacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'comentario': forms.Textarea(attrs={'class':'form-control'}),
            
        }
        labels = {
            'nombre':'', 'comentario':'', 'imágen': 'calificacion'
        }
