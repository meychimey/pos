# Generated by Django 3.1.12 on 2023-02-23 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_keranjang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keranjang',
            name='id_barang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.barang'),
        ),
        migrations.CreateModel(
            name='Laporan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(null=True)),
                ('id_keranjang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.keranjang')),
            ],
        ),
    ]
