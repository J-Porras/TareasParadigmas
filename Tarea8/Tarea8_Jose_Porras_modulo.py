# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 01:02:00 2021

@author: Porras
"""
import numpy
import pandas


def pregunta1():
    total = 0
    for n in range(150):
        if n%7==0:
            total = total + n
    return total
        
    

def pregunta2():
    lista = []
    n = 1024
    while n > 1:
           n = n//2
           lista.append(n)
    return lista
    
  



def pregunta3(a,b,c):
    if(isinstance(a,str) and isinstance(b,str) and isinstance(c,str)):
        return a +" " + b + " " + c
    return None


def isograma(string):
    if type(string) is not str:
        return str(string) + "No es un string"
                
    if(len(string)==0):
        return string + " es isograma"
    letras = set()
    for char in string.lower():
        if char in letras:
            return string + " no es isograma"
        else:
            letras.add(char)
    return string + " es isograma"

    
def esprimo(n):
    if n == 2 or  n == 3:
        return True
    if n > 3:
        for i in range(2, (n//2)+1):
            if (n % i) == 0:
                return False
            else:
                return True
    else:
        return False
        


def smallprime(lista):
    if(type(lista) is not list):
        return 0
    else:

        if len(lista) == 0:
            return 0
        else:
            num = max(lista)
            for n in lista:
             if esprimo(n) == True:
                if n < num:
                    num = n
        return num
            


def pregunta7(c):
    if type(c) is not str:
        return False
    else:
        nuevostring = ""
        vocales = ["a","e","i","o","u"]
        for char in c:
            if not (char.lower() in vocales):
                nuevostring = nuevostring + char
        return nuevostring


def pregunta8(vec,n):
    if type(vec) is not list:
        return 0
    else:
        porcen = {}
        menorigual = 0
        mayor = 0
        for num in vec:
            if num > n:

                mayor  = mayor + 1
            if num <= n:
                menorigual = menorigual +1

        porcen["Menores o iguales"] = menorigual / len(vec)
        porcen["Mayores"] = mayor / len(vec)
        return porcen



def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        return result

def pregunta9(n):
    if n < 0:
        return False
    else:
        vec = []
        while n!=1:
            vec.append(n)
            n = collatz(int(n))
        vec.append(n)
    return vec


def cuadrada (m): return all (len (row) == len (m) for row in m)

def diagonal(matrix):
    if not cuadrada(matrix):
        return False
    
    m = len(matrix)
    if m == 1: return matrix[0][0]
    count = 0
    for i in range(m):
      count += matrix[i][i]
    return count

def estadisticasCol(DF,nc):
    
    media = numpy.mean(DF.iloc[:,nc])
    mediana = numpy.median(DF.iloc[:,nc])
    deviacion = numpy.std(DF.iloc[:,nc])
    varianza = numpy.var(DF.iloc[:,nc])
    maximo = numpy.max(DF.iloc[:,nc])
    minimo = numpy.min(DF.iloc[:,nc])
    return {'Variable' : DF.columns.values[nc],
            'Media' : media,
            'Mediana' : mediana,
            'DesEst' : deviacion,
            'Varianza' : varianza,
            'Maximo' : maximo,
            'Minimo' : minimo}





def correlacionCols(DF,col1,col2):
    return numpy.correlate(numpy.ravel(DF.iloc[:,col1]),numpy.ravel(DF.iloc[:,col2]))

