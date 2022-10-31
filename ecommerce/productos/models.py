from django.db import models

# Create your models here.
from django.utils.html import format_html


class Producto(models.Model):
	# -------------------- Choices ------------------------------
	
	HO = 'HOMBRES'
	MU = 'MUJERES'
	NI = "NINOS"
	
	GENERO_CHOICES = [
		(HO, 'Hombre'),
		(MU, 'Mujeres'),
		(NI, "Ninos")
		]
	
	RO = 'ROJO'
	AZ = 'AZUL'
	VE = 'VERDE'
	AM = 'AMARILLO'
	MO = 'MOSTAZA'
	BO = 'BORDO'
	NE = 'NEGRO'
	BL = 'BLANCO'
	
	COLOR_CHOICES = [
		(RO, "Rojo"),
		(AZ, "Azul"),
		(VE, "Verde"),
		(AM, "Amarillo"),
		(MO, "Mostaza"),
		(BO, "Bordo"),
		(NE, "Negro"),
		(BL, 'Blanco')
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
	nombre_producto = models.CharField(max_length=50)
	imagen = models.ImageField(verbose_name='imagen')
	genero = models.CharField(verbose_name='genero', max_length=10, choices=GENERO_CHOICES)
	fecha_agregado = models.DateTimeField(verbose_name='date', auto_now_add=True)
	tipo_de_prenda = models.CharField(verbose_name='prenda', max_length=50, choices=PRODUCTOS_CHOICES)
	color = models.CharField(verbose_name='color', max_length=35, choices=COLOR_CHOICES)
	talle = models.CharField(verbose_name='talle', max_length=5, choices=TALLES_CHOICES)
	valor = models.FloatField(verbose_name='valor')
	stock = models.IntegerField(default=0)
	
	def __str__(self):
		return f"{self.id} - {self.nombre_producto}"
	
	# Stock formatted
	def stocks(self):
		if self.stock < 10:
			return format_html('<a style="color: #f00;">{}</a>', f"{self.stock}. Reponer mercaderia.")
		else: return self.stock
