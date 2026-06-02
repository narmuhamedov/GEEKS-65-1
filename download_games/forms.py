from django import forms
from . import models

class GamesForm(forms.ModelForm):
    class Meta:
        model = models.Games
        fields = '__all__'

