# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 01:02:00 2021

@author: Porras
"""
import numpy
print("Pregunta 1")


def pregunta1():
    total = 0
    for n in range(150):
        if n%7==0:
            total = total + n
    print(total)
        
    
pregunta1()   

print("") 
print("Pregunta 2")

def pregunta2():
    lista = []
    n = 1024
    while n > 1:
           n = n//2
           lista.append(n)
    print(lista)
    
pregunta2()    



def pregunta3(a,b,c):
    if(isinstance(a,str) and isinstance(b,str) and isinstance(c,str)):
        return print(a +" " + b + " " + c)
    return print(None)
    
print("")
print("Pregunta 3")
pregunta3("The","Rolling","Stones")    
pregunta3(1,"Rolling","Stones")    
pregunta3(0,"Rolling","Stones") 


def isograma(string):
    if type(string) is not str:
        return print(str(string) + "No es un string")
                
    if(len(string)==0):
        return print(string + " es isograma")
    letras = set()
    for char in string.lower():
        if char in letras:
            return print(string + " no es isograma")
        else:
            letras.add(char)
    return print(string + " es isograma")
        
print(" ")        
print("Pregunta 4")

isograma("Pregunta")
isograma("abcdef")
isograma("isOgrAma")

    
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
        
  
print(" ")      
print("Pregunta 5")
   
print(esprimo(999331))
print(esprimo(1))
print(esprimo(88888888))
        


print(" ")      
print("Pregunta 6")


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
        print("" ,num)
            
                
smallprime([1,2,3,4,5,6,7,8,9,10])            
smallprime([2,3,5,7,11,13,17,19])            
smallprime([100,200,300,500,400,17,2])



print(" ")
print("Pregunta 7")

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

print(pregunta7("Hola Mundo"))
print(pregunta7("Vocales"))
print(pregunta7("aeÑiou"))

         

print("")
print("Pregunta 8")

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
        print(porcen)

pregunta8([1,2,3,4,5,2,3,4,5,5,5,6],2)
pregunta8([1,2,3,2],2)
pregunta8([1,2,3,2,2],2)

print(" ")
print("Pregunta 9")

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
    print(vec)

pregunta9(3)
pregunta9(12)
pregunta9(40)


print("")

def cuadrada (m): return all (len (row) == len (m) for row in m)

def diagonal(m):
    if not cuadrada(m):
        return False
    else:
        sum_2_diagonal = 0
        for x in range(0, len(m)):
            for y in range(0, len(m)):
                if x + y == m - 1:
                    sum_2_diagonal = sum_2_diagonal + m[x][y]
        return print(sum_2_diagonal)

diagonal(numpy.matrix([[0,20,6],[4,12,48],[-8,-5,-16]]))

