from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    # Customize the labels of the fields
    title = forms.CharField(label='Movie Title')
    release_date = forms.DateField(label='Release Date', help_text='Format: YYYY-MM-DD')

    # Customize the widget for a field (e.g., add a date picker for the release_date field)
    widgets = {
        'release_date': forms.DateInput(attrs={'type': 'date'})
    }
