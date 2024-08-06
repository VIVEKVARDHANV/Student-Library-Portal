from django import forms
from .models import PDFFilebe,PDFFilebme,PDFFilemaths,PDFFilechem,PDFFilemos

class PDFFileFormbe(forms.ModelForm):
    class Meta:
        model = PDFFilebe
        fields = ['title', 'pdf']
class PDFFileFormbme(forms.ModelForm):
    class Meta:
        model = PDFFilebme
        fields = ['title', 'pdf']
class PDFFileFormchem(forms.ModelForm):
    class Meta:
        model = PDFFilechem
        fields = ['title', 'pdf']
class PDFFileFormmaths(forms.ModelForm):
    class Meta:
        model = PDFFilemaths
        fields = ['title', 'pdf']
class PDFFileFormmos(forms.ModelForm):
    class Meta:
        model = PDFFilemos
        fields = ['title', 'pdf']