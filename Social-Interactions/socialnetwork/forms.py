from django import forms

from models import Item

MAX_UPLOAD_SIZE = 2500000

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
       

