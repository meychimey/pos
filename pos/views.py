from django.shortcuts import render, redirect
from pos.models import *
# from pos.forms import FromBuku
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


def sigup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat")
            return redirect('sigup')
        
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('sigup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form,
        }
        return render(request, 'sigup.html', konteks)

# @Login_required(login_url=settings.LOGIN_URL)
def kasir(request):
    return render(request, 'kasir.html')

# @Login_required(login_url=settings.LOGIN_URL)
def barang(request):
    return render(request, 'barang.html')

# @Login_required(login_url=settings.LOGIN_URL)
def keranjang(request):
    return render(request, 'keranjang.html')

# @Login_required(login_url=settings.LOGIN_URL)
def laporan(request):
    return render(request, 'laporan.html')

# @Login_required(login_url=settings.LOGIN_URL)
def home(request):
    return render(request, 'home.html')



# Create your views here.
