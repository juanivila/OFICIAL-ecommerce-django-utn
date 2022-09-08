from django.db import models

# Create your models here.
from django.utils.html import format_html


class Producto(models.Model):
	# -------------------- Choices ------------------------------
	
	# ---- Colores ----
	RO = 'ROJO'
	AZ = 'AZUL'
	VE = 'VERDE'
	AM = 'AMARILLO'
	MO = 'MOSTAZA'
	BO = 'BORDO'
	
	COLOR_CHOICES = [
		(RO, "Rojo"),
		(AZ, "Azul"),
		(VE, "Verde"),
		(AM, "Amarillo"),
		(MO, "Mostaza"),
		(BO, "Bordo")
		]
	# ---- Talles ----
	XS = "XS"
	S = "S"
	M = "M"
	L = "L"
	XL = "XL"
	XXL = "XXL"
	
	TALLES_CHOICES = [
		(XS, 'XS'),
		(S, 'S'),
		(M, 'M'),
		(L, 'L'),
		(XL, 'XL'),
		(XXL, 'XXL')
		]
	
	# ---- Productos ----
	RE = "REMERA"
	BU = "BUZO"
	CA = "CAMPERA"
	PA = "PANTALON"
	BE = "BERMUDAS"
	AC = "ACCESORIOS"
	
	PRODUCTOS_CHOICES = [
		(RE, "Remera"),
		(BU, "Buzo"),
		(CA, "Campera"),
		(PA, "Pantalon"),
		(BE, "Bermudas"),
		(AC, "Accesorios")
		
		]
	
	# -------------------- Models ------------------------------
	nombre_producto = models.CharField(verbose_name='producto', max_length=50)
	tipo_de_prenda = models.CharField(verbose_name='prenda', max_length=50, choices=PRODUCTOS_CHOICES)
	color = models.CharField(verbose_name='color', max_length=35, choices=COLOR_CHOICES)
	talle = models.CharField(verbose_name='talle', max_length=5, choices=TALLES_CHOICES)
	valor = models.ForeignKey("Valor", on_delete=models.CASCADE, default=0)
	stock = models.IntegerField(default=0)
	
	def __str__(self):
		return f"{self.id} - {self.nombre_producto}"
	
	# Stock formatted
	def stocks(self):
		if self.stock < 10:
			return format_html('<a style="color: #f00;">{}</a>', f"{self.stock}. Reponer mercaderia.")
		else: return self.stock


class Valor(models.Model):
	precio_de_venta = models.DecimalField(decimal_places=2, max_digits=6)
	costo_de_adquisicion = models.DecimalField(decimal_places=2, max_digits=6)
	
	def __str__(self):
		return f"Venta: ${self.precio_de_venta} Costo: ${self.costo_de_adquisicion}"
