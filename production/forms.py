from django import forms

from .models import Prod
from .models import Machine

class ProdForm(forms.ModelForm):

    class Meta():
        model = Prod
        fields = ("Objectif", "Output")

        widgets= {
            'Objectif': forms.NumberInput(
                attrs={
                    'placeholder':'Objectif',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                    'value': '514'
                }
            ),
            'Output': forms.NumberInput(
                attrs={
                    'placeholder': 'Output',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),






        }