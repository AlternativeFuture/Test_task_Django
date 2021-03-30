from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description"]


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description", "completed"]

