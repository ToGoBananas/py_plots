from django import forms
from .models import PlotFunction


class PlotFunctionForm(forms.Form):
    field1 = forms.ModelChoiceField(queryset=PlotFunction.objects.all())
