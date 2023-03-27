from django.shortcuts import render, redirect
from django.db.models import Sum
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
    # delete nama barang
    kasir = Keranjang.objects.all()
    byr  = Keranjang.objects.aggregate(Sum('bayar'))['bayar__sum'] or 0
    subt = Keranjang.objects.aggregate(total=Sum('id_barang__harga_barang'))['total'] or 0
    kembalian = byr-subt


    if request.POST: 
        form = FormKeranjang(request.POST)
        
        if form.is_valid():
            form.save()
            
        
        konteks = {
        'form':form,
        'kembalian':kembalian,
        'byr':byr,
        'subt':subt,
        'kasir': kasir
        }
        return redirect( '/kasir',konteks)
      
    else:
        form = FormKeranjang()
        konteks = {
            'form':form,
            'kembalian':kembalian,
            'byr':byr,
            'subt':subt,
            'kasir': kasir,
           
        }
            
        return render (request,'kasir.html',konteks)
   
def selesai(request):
    Keranjang.objects.all().delete()

    messages.success(request, 'Transaksi selesai!')
    return redirect('/kasir')

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

def hapus_barang(request, id):
    barang = Barang.objects.get(id=id)
    barang.delete()
    return redirect('/barang')