from django import forms

from station.models import Station

class AjouForm(forms.ModelForm):



    class Meta():
        model = Station
        fields = ('Num_station', 'id_machine')

        widgets= {
            'Num_station': forms.TextInput(
                attrs={
                    'placeholder':'Num_station',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),

            'id_machine': forms.NumberInput(
                attrs={
                    'placeholder': 'id_machine',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),




        }