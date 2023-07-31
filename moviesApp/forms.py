from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['title', 'release_date', 'director', 'genre']

    # Customize the labels of the fields
    title = forms.CharField(label='Movie Title')
    release_date = forms.DateField(label='Release Date', help_text='Format: YYYY-MM-DD')

    # Customize the widget for a field (default is TextInput)
    widgets = {
        'release_date': forms.DateInput(attrs={'type': 'date'})
    }
