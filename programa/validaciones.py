#!/usr/bin/python
# -*- coding: latin-1 -*-
import ayuda
import vigenere
import archivo
import cesar
import afin

def validacionCesar(argumentos):
	if(len(argumentos)!=6):
		print "\nEl numero de parametros es incorrecto"
		print "Revisar la ayuda del algoritmo de cesar: python principal.py -sc\n"
	else:
		if(argumentos[2]=="-c"):
			f = archivo.abrirArchivo(argumentos[3])
			if f=='':
				print 'No se encontro el archivo '+argumentos[3]
			else:
				texto = ((f.read().replace(' ','')).rstrip('\n')).upper()
				f.close()
				clave = cesar.obtenerEntero(argumentos[4])
				if(clave != -1):
					cesar.cifrarCesar(texto, clave, argumentos[5])
		elif(argumentos[2]=="-d"):
			f = archivo.abrirArchivo(argumentos[3])
			if f=='':
				print 'No se encontro el archivo '+argumentos[3]
			else:
				texto = ((f.read().replace(' ','')).rstrip('\n')).upper()
				f.close()
				clave = cesar.obtenerEntero(argumentos[4])
				if(clave != -1):
					cesar.descifrarCesar(texto, clave, argumentos[5])
		else: 
			print "\nEl modo ",argumentos[2]," es incorrecto"
			print "Revisar la ayuda del algoritmo de cesar: python principal.py -sc\n"

def validacionAfin(argumentos):
	if(len(argumentos)!=7):
		print "\nEl numero de parametros es incorrecto"
		print "Revisar la ayuda del algoritmo de afin: python principal.py -sa\n"
	else:
		if(argumentos[2]=="-c"):
			f = archivo.abrirArchivo(argumentos[3])
			if f=='':
				print 'No se encontro el archivo '+argumentos[3]
			else:
				texto = ((f.read().replace(' ','')).rstrip('\n')).upper()
				f.close()
				a = afin.obtenerA(argumentos[4])
				if (a != -1):
					if (afin.verificarCoprimo(a) != True):	
						print 'El nuemero a es invalido'
						print 'El numero debe ser primo con el tamano del alfabeto' 
					else:
						b = afin.obtenerB(argumentos[5])
						if(b != -1):
							afin.cifrarAfin(texto, a, b, argumentos[6])
		elif(argumentos[2]=="-d"):
			f = archivo.abrirArchivo(argumentos[3])
			if f=='':
				print 'No se encontro el archivo '+argumentos[3]
			else:
				texto = ((f.read().replace(' ','')).rstrip('\n')).upper()
				f.close()
				a = afin.obtenerA(argumentos[4])
				if (a != -1):
					if (afin.verificarCoprimo(a) != True):	
						print 'El nuemero a es invalido'
						print 'El numero debe ser primo con el tamano del alfabeto' 					
					else:					
						b = afin.obtenerB(argumentos[5])
						if(b != -1):
							afin.descifrarAfin(texto, a, b, argumentos[6])
		else: 
			print "\nEl modo ",argumentos[2]," es incorrecto"
			print "Revisar la ayuda del algoritmo de afin: python principal.py -sa\n"

def validacionVigenere(argumentos):
	if(len(argumentos)!=6):
		print "\nEl numero de parametros es incorrecto"
		print "Revisar la ayuda del algoritmo de vigenere: python principal.py -sva\n"
	else:
		if(argumentos[2]=="-c"):
			#print "cifrar"
			vigenere.cifraVigenere(argumentos[3],argumentos[4],argumentos[5])
		elif(argumentos[2]=="-d"):
			#print "descifrar"
			vigenere.descVigenere(argumentos[3],argumentos[4],argumentos[5])
		else: 
			print "\nEl modo ",argumentos[2]," es incorrecto"
			print "Revisar la ayuda del algoritmo de vigenere: python principal.py -sva\n"
