from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Enter your name', max_length=100)
