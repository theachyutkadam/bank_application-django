from django import forms
from .models import Manager

from manager.models import Manager
class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = "__all__"
