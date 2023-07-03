from django import forms

from .models import Scrap

class Scrapform(forms.ModelForm):



    class Meta():
        model = Scrap
        fields = ('Occurence', 'id_problem',)

        widgets= {
            'Occurence': forms.NumberInput(
                attrs={
                    'placeholder':'Occurence',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),

            'id_problem': forms.TextInput(
                attrs={
                    'placeholder': 'id_problem',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),

        }