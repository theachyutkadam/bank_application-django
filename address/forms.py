from django import forms
from address.models import Address
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
