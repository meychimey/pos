from django.db import models

# Create your models here.
class Barang(models.Model):
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.IntegerField(null=True)
    tgl_input = models.DateTimeField(auto_now=True, null=True)
    foto = models.ImageField(upload_to='barang', null=True)

    def __str__(self):
        return self.nama_barang

class Keranjang(models.Model):
    id_barang = models.ForeignKey(Barang, on_delete=models.CASCADE, null=True)
    quintity = models.IntegerField(null=True)
    # subtotal = models.IntegerField(null=True)
    tgl = models.DateTimeField(auto_now=True, null=True)
    no_transaksi = models.IntegerField(null=True)
    bayar = models.IntegerField(null=True)
    # kembalian = models.IntegerField()
    def subtotal(self): 
        subtotal = self.id_barang.harga_barang * self.quintity
        
        return subtotal
    def kembalian(self):
          subtotal = self.subtotal()
          return self.bayar - subtotal
          
class Laporan(models.Model):
    id_keranjang = models.ForeignKey(Keranjang, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(null=True)
