from django import forms
from .models import dj_srk

class dj_form(forms.ModelForm):
    gen = (("Male","Male"), ("Female", "Female"), ("Others", "Others"))
    gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)

    ct = (("Thane", "Thane"), ("Dombivali", "Dombivali"), ("Kalyan", "Kalyan"), ("Ambernath", "Ambernath"), ("Badlapur", "Badlapur"))
    city = forms.ChoiceField(choices=ct, widget=forms.Select)
    
    class Meta:
        model = dj_srk
        fields ='__all__'