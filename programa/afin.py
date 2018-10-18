#!/usr/bin/python
# -*- coding: utf-8 -*-
import archivo

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc = abc.decode('utf8')
ene = 'Ñ'.decode('utf8')
eneAux = ene.encode('utf8')
TAM_MAX_CLAVE = len(abc)

def cifrarAfin(texto, a, b, salida):
	mensajeCifrado = ""
	posicion = 0
	texto = texto.decode('utf8')
	#print '\nEL TEXTO EN CLARO ES: ',texto
	for caracter in texto: 
		if caracter == ene:
			caracter = 'N'
		mi = abc.find(caracter)
		modulo = (a*mi+b)%len(abc)
		mensajeCifrado = mensajeCifrado + abc[modulo]
	#print 'Ingrese el nombre del archivo donde se guardara el criptograma'
	n = salida
	mensajeCifrado = mensajeCifrado.encode('utf8')
	f = archivo.escribirArchivo(n,mensajeCifrado)
	if f=='':
		print 'Ocurrio un error al intentar escribir en ', n
	else:
		print 'Se guardo correctamente el mensaje cifrado en ', n
		f.close()

def descifrarAfin(texto, a, b, salida):
	d,x,y = extMcd(a,len(abc))
	mensajeClaro = ""
	texto = texto.decode('utf8')
	for caracter in texto:
		if caracter == eneAux:
			caracter = 'Ñ'
		ci = abc.find(caracter)
		modulo = (x*(ci-b))%len(abc)
		mensajeClaro = mensajeClaro + abc[modulo]
	#print 'Ingrese el nombre del archivo donde se guardara el mensaje en claro'
	n = salida
	mensajeClaro = mensajeClaro.encode('utf8')
	f = archivo.escribirArchivo(n,mensajeClaro)
	if f=='':
		print 'Ocurrio un error al intentar escribir en ', n
	else:
		print 'Se guardo correctamente el mensaje descifrado en ',n
		f.close()
	
def verificarCoprimo(a):
	d,x,y = extMcd(a,len(abc))
	if d == 1:
		return True
	else:
		return False
	
def extMcd(a,b):
	if b == 0:
		return a,1,0
	x2 = 1
	x1 = 0
	y2 = 0
	y1 = 1
	while b != 0:
		q = a//b
		r = a - q*b
		x = x2 - q*x1
		y = y2 - q*y1
		a = b
		b = r
		x2 = x1
		x1 = x
		y2 = y1
		y1 = y
	if a < 0:
		return map(int, (-a, -x2, -y2))
	return map(int, (a, x2, y2))
	
def obtenerA(valor):
	a = 0
	try:
		a = int(valor)
	except ValueError:
		print "Ingresa un numero entre 1 y ",TAM_MAX_CLAVE-1," para 'a'\n"
		return -1
	else:
		if (a >= 0 and a < len(abc)):
			return a
		else:
			print 'Ingresa un numero entre 1 y ',TAM_MAX_CLAVE-1," para 'a'\n"
			return -1

def obtenerB(valor):
	a = 0
	try:
		a = int(valor)
	except ValueError:
		print "Ingresa un numero entre 1 y ",TAM_MAX_CLAVE-1," para 'b'\n"
		return -1
	else:
		if (a >= 0 and a < TAM_MAX_CLAVE):
			return a
		else:
			print 'Ingresa un numero entre 1 y ', TAM_MAX_CLAVE-1," para 'b'\n"
			return -1
