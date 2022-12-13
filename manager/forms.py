from django import forms
from manager.models import Manager
class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = "__all__"
