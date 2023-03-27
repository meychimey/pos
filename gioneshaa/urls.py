from django.contrib import admin
from django.urls import path
from pos.views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('selesai/', selesai, name='selesai'), 
    path('hapus/<int:id>', hapus_barang, name='hapus_barang'), 
    path('kasir/', kasir,name='kasir'),
    path('barang/', barang,name='barang'),
    path('laporan/', laporan),
    path('login/', LoginView.as_view(), name='login'),
    path('logut/', LogoutView.as_view(next_page='home'), name='logout'),
    path('sigup/', sigup, name='sigup'),
]
