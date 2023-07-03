from django import forms

from .models import Down

class DTForm(forms.ModelForm):

    class Meta:
        model = Down
        fields = ("Durée", "commentaire", "id_station")

        widgets= {

            'Durée': forms.NumberInput(
                attrs={
                    'placeholder': 'Durée',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),

            'commentaire': forms.TextInput(
                attrs={
                    'placeholder': 'commentaire',
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