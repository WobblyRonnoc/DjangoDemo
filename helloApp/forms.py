from django import forms


class MyForm(forms.Form):
    input_field = forms.CharField(label='Enter your name', max_length=100)
