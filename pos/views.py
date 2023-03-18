from django.shortcuts import render, redirect
from pos.models import *
from pos.form import FormKeranjang,FormBarang
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
    kasir = Keranjang.objects.all()

    if request.POST: 
        form1 = FormKeranjang(request.POST)
        
        if form1.is_valid():
            form1.save()
            
        
        konteks = {
        'form':form,
        'kasir': kasir
        }
        return redirect( '/kasir',konteks)
      
    else:
        form = FormKeranjang()
        konteks = {
            'form':form,
            'kasir': kasir,
           
        }
            
        return render (request,'kasir.html',konteks)
   

# @Login_required(login_url=settings.LOGIN_URL)
def barang(request):
    #nambah barang
    barang = Barang.objects.all()
    if request.POST:
        form = FormBarang(request.POST)
        if form.is_valid():
            form.save()
        konteks = {
            'form':form,
            'barang':barang
        }
        return redirect('/barang',konteks)
    else:
        form = FormBarang()
        konteks = {
            'form':form,
            'barang':barang
        }
        return render(request, 'barang.html',konteks)



# @Login_required(login_url=settings.LOGIN_URL)
def laporan(request):
    return render(request, 'laporan.html')

# @Login_required(login_url=settings.LOGIN_URL)
def home(request):
    return render(request, 'home.html')

