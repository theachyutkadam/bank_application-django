from django import forms
from particular_detail.models import ParticularDetail
class ParticularDetailForm(forms.ModelForm):
    class Meta:
        model = ParticularDetail
        fields = "__all__"
