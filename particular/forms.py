from django import forms
from particular.models import Particular
class ParticularForm(forms.ModelForm):
    class Meta:
        model = Particular
        fields = "__all__"
