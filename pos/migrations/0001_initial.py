# Generated by Django 3.1.12 on 2023-02-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=50)),
                ('harga_barang', models.IntegerField(null=True)),
                ('tgl_input', models.DateTimeField(null=True)),
            ],
        ),
    ]
