from django import forms
from nominee.models import Nominee
class NomineeForm(forms.ModelForm):
    class Meta:
        model = Nominee
        fields = "__all__"
