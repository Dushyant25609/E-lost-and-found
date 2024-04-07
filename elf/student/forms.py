# forms.py

from django import forms
from .models import Found_Item, Lost_Item

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = Found_Item
        fields = ['name', 'enrollment_no', 'phone_no', 'item_name', 'item_description', 'image', 'location', 'date']

class LostItemForm(forms.ModelForm):
    class Meta:
        model = Lost_Item
        fields = ['name', 'enrollment_no', 'phone_no', 'item_name', 'item_description', 'image', 'location', 'date']
