from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        labels = {
            'laptop_id': 'LAPTOP ID',
            'name': 'NAME',
            'brand': 'BRAND',
            'ram': 'RAM',
            'rom': 'ROM',
            'price': 'PRICE',
            'processor': 'PROCESSOR',
            'color': 'COLOR'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'eg. Pavilion, Inspiron etc'
            }),
            'brand': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'eg. DELL, HP, etc'
            }),
            'ram': forms.TextInput(attrs={
                'autocomplete': 'off',

            }),
            'rom': forms.TextInput(attrs={
                'autocomplete': 'off',

            }),
            'price': forms.NumberInput(attrs={
                'autocomplete': 'off',

            }),
            'processor': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'eg. Intel i5, i7 etc'
            }),
            'color': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'eg. Gray, Silver etc'
            })
        }