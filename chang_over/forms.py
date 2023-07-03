from django import forms

from .models import Change

class ChangeForms(forms.ModelForm):

    class Meta:
        model = Change
        fields = ('Durée', 'id_station')

        widgets= {

            'Durée': forms.NumberInput(
                attrs={
                    'placeholder': 'Durée',
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