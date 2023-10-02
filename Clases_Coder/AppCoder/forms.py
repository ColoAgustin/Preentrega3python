from django import forms
from .models import Pilotos
from .models import Fechas
class PilotosFormulario(forms.Form):
    nombre  = forms.CharField()
    apellido = forms.IntegerField()

class BuscaPilotosForm(forms.Form):
    pilotos = forms.CharField()
