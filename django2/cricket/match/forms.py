from django import forms
from match.models import Match

class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = '__all__'