from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta: 
        model = Task
        fields = ['participacion', 'nombre_completo', 'edad', 'calle_y_numero', 'colonia', 'c_p', 'municipio', 
                  'estado', 'num_seccion', 'num_casilla', 'nombre_enlace', 'description', 'datecompleted']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        widgets = {
            'participacion': forms.Select(attrs={'class': 'form-control'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.Select(attrs={'class': 'form-control'}),
            'calle_y_numero': forms.TextInput(attrs={'class': 'form-control'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control'}),
            'c_p': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'num_seccion': forms.Select(attrs={'class': 'form-control'}),
            'num_casilla': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_enlace': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
            }
        
        
        