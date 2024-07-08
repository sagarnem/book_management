from django import forms
from users.models import UserBalance

class UserBalanceForm(forms.ModelForm):
    class Meta:
        model = UserBalance
        fields = ['user','balance']