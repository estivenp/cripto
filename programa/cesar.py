#!/usr/bin/python
# -*- coding: utf-8 -*-
import archivo

abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
abc = abc.decode('utf8')
ene = 'Ñ'.decode('utf8')
eneAux = ene.encode('utf8')
TAM_MAX_CLAVE = len(abc)
	
def cifrarCesar(texto, clave, salida):
	mensajeCifrado = ""
	posicion = 0
	texto = texto.decode('utf8')
	for caracter in texto: 
		if caracter == ene:
			caracter = 'N'
		mi = abc.find(caracter)
		modulo = (mi+clave)%len(abc)
		mensajeCifrado = mensajeCifrado + abc[modulo]
	#print 'Ingresa el nombre del archivo donde se guardara el criptograma'
	n = salida
	mensajeCifrado = mensajeCifrado.encode('utf8')
	f = archivo.escribirArchivo(n, mensajeCifrado)
	if f =='':
		print 'Ocurrio un error al intentar escribir en ', n
	else:
		print 'El mensaje cifrado se guardo correctamente en ',n
		f.close()

def descifrarCesar(criptograma, clave,salida):
	mensajeClaro = ""
	criptograma = criptograma.decode('utf8')
	for caracter in criptograma:
		if caracter == eneAux:
			caracter = 'Ñ'
		ci = abc.find(caracter)
		modulo = (ci-clave)%len(abc)
		mensajeClaro = mensajeClaro + abc[modulo]
	#print 'Ingresa el nombre del archivo donde se guardara el mensaje en claro'
	n = salida
	mensajeClaro = mensajeClaro.encode('utf8')
	f = archivo.escribirArchivo(n, mensajeClaro)
	if f=='':
		print 'Ocurrio un error al intentar escribir en ', n
	else:
		print 'El mensaje descifrado se guardo correctamente en ',n
		f.close()	
	
def obtenerEntero(cla):
	clave = 0
	try:
		clave = int(cla)
	except ValueError:
		print "Ingresa un numero entre 1 y \n",TAM_MAX_CLAVE-1
		return -1
	else:
		if (clave >= 0 and clave < TAM_MAX_CLAVE):
			return clave
		else:
			print 'Ingresa un numero entre 1 y \n', TAM_MAX_CLAVE-1
			return -1
		

def cifrarDescifrar():
	accion = 0
	print '\n1. Cifrar \n2. Descifrar \n3. Regresar'
	try:
		accion = int(input('\nIngresa una opcion: '))
	except NameError:
		print "Debes ingresar un numero entre 1 y 3"
	else:
		if accion >= 1 and accion <=3:
			return accion
		else:
			print 'Debes ingresar un numero entre 1 y 3'
