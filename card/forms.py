from django import forms
from card.models import Card
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"
