from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta():
        model=Item
        fields='__all__'

        widgets = {
    'item_name': forms.TextInput(attrs={
        'class': 'w-full bg-transparent text-gray-800 border-2 border-gray-800 rounded-lg p-3 focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500'
    }),
    'item_desc': forms.Textarea(attrs={
        'class': 'w-full bg-transparent text-gray-800 border-2 border-gray-800 rounded-lg p-3 h-24 focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500'
    }),
    'item_price': forms.NumberInput(attrs={
        'class': 'w-full bg-transparent text-gray-800 border-2 border-gray-800 rounded-lg p-3 focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500'
    }),
    'item_quantity': forms.NumberInput(attrs={
        'class': 'w-full bg-transparent text-gray-800 border-2 border-gray-800 rounded-lg p-3 focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500'
    }),
    'item_img': forms.TextInput(attrs={
        'class': 'w-full bg-transparent text-gray-800 border-2 border-gray-800 rounded-lg p-3 focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500'
    }),
}