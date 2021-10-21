from django import forms
from main.models import Utilisateur

class Userform(forms.ModelForm):
    class Meta :
        model = Utilisateur
        fields = ('nom' , 'prenom' ,'sexe' , 'email' , 'phone' , 'photo')