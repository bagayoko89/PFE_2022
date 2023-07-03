from django import forms

from .models import Val

class ValForm(forms.ModelForm):

    class Meta:
        model = Val
        fields = ("Dur",)

        widgets= {

            'Dur': forms.NumberInput(
                attrs={
                    'placeholder': 'Durée',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),



        }