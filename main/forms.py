from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):

    JERSEY_TYPE = {
        "club": "Club Jersey",
        "nation": "Nation Jersey",
    }

    class Meta:
        model = Product
        fields = ["name", "price", "description", "type"]