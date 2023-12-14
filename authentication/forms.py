from django import forms

class profileForm(forms.Form):
    name = forms.CharField(max_length=60)
    email = forms.EmailField()
    psw = forms.CharField(max_length=50)