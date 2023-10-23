from django import forms
from .models import Reviews

class RewiewForm(forms.ModelForm):
    '''Форма отзывов'''
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text_reviews')
