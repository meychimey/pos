# Generated by Django 3.1.12 on 2023-03-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_auto_20230223_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='foto',
            field=models.ImageField(null=True, upload_to='barang'),
        ),
        migrations.AlterField(
            model_name='barang',
            name='tgl_input',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='keranjang',
            name='kembalian',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='keranjang',
            name='tgl',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
