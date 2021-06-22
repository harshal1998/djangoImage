from django import forms
from .models import *


class hotelform(forms.ModelForm):
    class Meta:
        model = hotel
        fields = "__all__"
