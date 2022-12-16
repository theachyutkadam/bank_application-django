from django import forms
from account_type.models import AccountType
class AccountTypeForm(forms.ModelForm):
    class Meta:
        model = AccountType
        fields = "__all__"
