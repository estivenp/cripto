#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

Alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x'
,'y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X'
,'Y','Z','0','1','2','3','4','5','6','7','8','9','.',',',' ','\n','_','[',']']

def agregarSimbolo(simbolo):	
	#print '\xc3'
	Alfabeto.append(simbolo)

def imprimir():
	print Alfabeto

def getAlfabeto():
	return Alfabeto
def tamAlfabeto():
	return len(Alfabeto)

#print Alfabeto.index('Ñ')
#imprimir()
