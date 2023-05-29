from django import forms
from .models import DeviceInformation


class UpdateForm(forms.ModelForm):
    class Meta:
        model = DeviceInformation
        fields = ('total','worked','broke','timestamp')

