from django.forms import ModelForm
from pos.models import Keranjang,Barang
from django import forms
from django.contrib.auth.models import User

class FormKeranjang(ModelForm):
    class Meta:
        model = Keranjang
        fields = '__all__'
        widgets = {
            'quintity': forms.TextInput(attrs={'class': 'form-control'}),
            'no_transaksi': forms.TextInput(attrs={'class': 'form-control'}),
            'bayar': forms.TextInput(attrs={'class': 'form-control'}),
            
            
        }

class FormBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        
      