from django.forms import ModelForm
from pos.models import Keranjang

class FormKeranjang(ModelForm):
    class Meta:
        model = Keranjang
        fields = '__all__'