# Generated by Django 4.1.1 on 2022-10-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=50, verbose_name='producto')),
                ('imagen', models.ImageField(upload_to='', verbose_name='imagen')),
                ('genero', models.CharField(choices=[('HOMBRES', 'Hombre'), ('MUJERES', 'Mujeres'), ('NINOS', 'Ninos')], max_length=10, verbose_name='genero')),
                ('fecha_agregado', models.DateTimeField(verbose_name='date')),
                ('tipo_de_prenda', models.CharField(choices=[('REMERA', 'Remera'), ('BUZO', 'Buzo'), ('CAMPERA', 'Campera'), ('PANTALON', 'Pantalon'), ('BERMUDAS', 'Bermudas'), ('ACCESORIOS', 'Accesorios')], max_length=50, verbose_name='prenda')),
                ('color', models.CharField(choices=[('ROJO', 'Rojo'), ('AZUL', 'Azul'), ('VERDE', 'Verde'), ('AMARILLO', 'Amarillo'), ('MOSTAZA', 'Mostaza'), ('BORDO', 'Bordo')], max_length=35, verbose_name='color')),
                ('talle', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=5, verbose_name='talle')),
                ('valor', models.FloatField(verbose_name='valor')),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
