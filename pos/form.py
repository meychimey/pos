from django.forms import ModelForm
from pos.models import Keranjang,Barang

class FormKeranjang(ModelForm):
    class Meta:
        model = Keranjang
        fields = '__all__'

class FormBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'