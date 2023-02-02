from .models import todo
from django import forms


class form1(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['name', 'priority', 'date']
