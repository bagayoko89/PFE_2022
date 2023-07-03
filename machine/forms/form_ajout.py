from django import forms

from machine.models import Machine

class AjoutForm(forms.ModelForm):



    class Meta():
        model = Machine
        fields = ('nom',)

        widgets= {
            'nom': forms.TextInput(
                attrs={
                    'placeholder':'nom',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),




        }