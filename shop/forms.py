from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta: # used ChatGPT
        model = Product
        fields = ['name', 'description', 'price'] 
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }




