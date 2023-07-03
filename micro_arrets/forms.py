from django import forms

from .models import Micro

class MicroForms(forms.ModelForm):

    class Meta:
        model = Micro
        fields = ('frequence', 'id_station')

        widgets= {

            'frequence': forms.NumberInput(
                attrs={
                    'placeholder': 'frequence',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),

            'id_station': forms.TextInput(
                attrs={
                    'placeholder': 'id_station',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),



        }