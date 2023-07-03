from django import forms

from .models import Prob

class Ajoutprob(forms.ModelForm):



    class Meta():
        model = Prob
        fields = ('id_problem', 'description', 'id_station', 'image')

        widgets= {
            'id_problem': forms.TextInput(
                attrs={
                    'placeholder':'id_problem',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),

            'description': forms.TextInput(
                attrs={
                    'placeholder': 'description',
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