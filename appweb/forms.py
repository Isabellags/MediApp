from django import forms
from .models import Contacto, Profesional


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__" #todos los campos del modelo aparecen en el form
        #fields = ["nombre", "email", "telefono"]


class ProfesionalForm(forms.ModelForm):

    class Meta:
        model = Profesional
        fields = "__all__"


        widgets = {
            "fecha_nacimiento" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }