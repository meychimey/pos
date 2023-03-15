from django.contrib import admin
from django.urls import path
from pos.views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('barang/', barang),
    path('keranjang/', keranjang,name='keranjang'),
    path('laporan/', laporan),
    path('', home,name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logut/', LogoutView.as_view(next_page='home'), name='logout'),
    path('sigup/', sigup, name='sigup'),
]
