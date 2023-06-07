from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import *
import datetime

# Form for the add and update a product
class addProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['proBoughtDate'].initial = datetime.date.today()

    class Meta:
        model = t_products
        fields = ['proName', 'proNote', 'proImage', 'proBoughtPrice', 'proBoughtDate', 'fkType' ,'fkCategory']
        labels = {
            'proName': 'Nom de produit :',
            'proNote': 'Description :',
            'proImage': 'Image :',
            'proBoughtPrice': 'Prix d\'achat :',
            'proBoughtDate': 'Date d\'achat :',
            'fkCategory': 'Categorie : ',
            'fkType': 'Type'
        }
        widgets = {
            'proBoughtDate': DateInput(format=('%Y-%m-%d'),attrs={'type': 'date', 'class': 'dateForm'}),
        }
        
class articleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = t_article
        fields = ['artName', 'artNote','fkRoom','fkProduct', 'fkCupboard']
        labels = {
            'artName': 'Label : ',
            'fkProduct': 'Produit : ',
            'artNote': 'Note : ',
            'fkRoom': 'Labo : ',
            'fkCupboard': 'Armoire : '
        }

class borrowForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['borDate'].initial = datetime.date.today()
        self.fields['borReturnDate'].initial = datetime.date.today() + datetime.timedelta(days=30)

    class Meta:
        model = t_borrow
        fields = ['borLocation', 'borDate', 'borReturnDate', 'borUser', 'fkArticle']
        labels = {
            'borLocation': 'Lieu demprunt :',
            'borDate': 'Date demprunt :',
            'borReturnDate': 'Date de retour :',
            'borUser': 'Emprunté par :',
            'fkArticle': 'Article :',
        }
        widgets = {
            'borDate': DateInput(format=('%Y-%m-%d'),attrs={'type': 'date', 'class': 'dateForm'}),
            'borReturnDate': DateInput(format=('%Y-%m-%d'),attrs={'type': 'date', 'class': 'dateForm'}),
        }
      