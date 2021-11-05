# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:52:08 2021

@author: Porras
"""
from cons import cons, car, cdr

# Pregunta 1
print("Pregunta 1")

def pregunta1(m,n):
    if m == 0:
        return 0
    if n == 0:
        return (2*m);
    if m == 1:
        return 2
    else:
        return pregunta1(n-1,pregunta1(n,m-1))
    
print(pregunta1(1,10))

print(pregunta1(2,4))
print(pregunta1(3,3))



print("")
print("Pregunta 2")

def pregunta2(n):
    if n == 1:
        return 0
    if (n%2) == 0:
        return pregunta2(n/2) +1
    else:
        return pregunta2(1+ (3*n)) + 1

    
print(pregunta2(16))  
print(pregunta2(12))    
print(pregunta2(31))


def pregunta2_iter(i,n):
    if n == 1:
        return i
    if (n%2)==0:
        return pregunta2_iter(i+1,n/2)
    else:
        return pregunta2_iter(i+1,1+(3*n))
    

def pregunta2(n):
    return pregunta2_iter(0,n)


print("")
print("Pregunta 2 Iterativo")
print(pregunta2(16))
print(pregunta2(12))
print(pregunta2(31))
               
     
               
print("")
print("Pregunta 3 ")

def pregunta3(n):
    if n == 0 :
        return 1
    if n  == 1:
        return 0
    if n  ==  2:
        return -1
    else:
        return (2*pregunta3(n-1) - (7 * pregunta3(n-2)) - 6*pregunta3(n-3))
    
    

print(pregunta3(4))
print(pregunta3(12))
print(pregunta3(13))

print("")
print("Pregunta 3 Iterativo ")
def pregunta3_iter_wrapper(n):
    return  pregunta3iter(0, -1, 1, 1,n)



def pregunta3iter(ant,res,transante,i,n):
    if i >= n:
        return ant
    else:
        return pregunta3iter(res,((2*res) - (7*ant) - (6*transante)),ant,(i+1),n )
    
    
print(pregunta3_iter_wrapper(4))   
print(pregunta3_iter_wrapper(12))  
print(pregunta3_iter_wrapper(13))   
 


print(" ")
print("Pregunta 4 Normal")


def productoria_normal(a, n):
  if(a  > n):
    return (1)
  
  else:
    return ((((7 * a) + ( a* a* a) - 11)  *  ((7 * a) + ( a* a* a) - 11) ) * (productoria_normal ((a + 1),n )))
  

print(productoria_normal(1,2))
print(productoria_normal(1,5))
print(productoria_normal(4,7))

print(" ")
print("Pregunta 4 Termino")



def cuadrado(a):
  return(a*a)

def cubo(a):
  return(a*a*a)

def productoria(f,a,n):
  if(a>n):
    return (1)
  else:
    return(f(a)*productoria(f,(a+1),n))
  


def termino(n):
  return (cuadrado(cubo(n)+(7*n)-11))


def productoria_termino(a, n):
  return (productoria(termino,a,n))


print(productoria_termino(1,2))
print(productoria_termino(1,5))
print(productoria_termino(4,7))



print(" ")
print("Pregunta 4 Lambda")


def productoria_lambda(a,n):
    return productoria(lambda x: cuadrado(cubo(x)+(7*x)-11),a,n)


print(productoria_lambda(1,2))
print(productoria_lambda(1,5))
print(productoria_lambda(4,7))



print(" ")
print("Pregunta 5")

def es_factor(x, k):
  if((x %k) == 0):
    return (True)
  
  return (False)
  

def suma_factores(x,k):
  if(k > ((x/2)+1)):
    return (0)
  
  else:
    if(es_factor(x,k)):
      return (k + suma_factores(x,(k+1)))
    
    else:
      return (suma_factores(x,(k+1)))
      

def clasificacion(n):
  if(suma_factores(n,1) == n):
    print("Perfecto")
  
  else:
    if(suma_factores(n,1) > n):
      print("Abundante")
    
    else:
      print("Defectivo")

clasificacion(12)
clasificacion(10)
clasificacion(6)


print(" ")
print("Pregunta 6")

def porcen_vector(lista, n):
  if(len(lista) == 0):
    return (0)
  
  else:
    if(car(lista) <= n):
      return(1 + porcen_vector(cdr(lista),n ) )
    
    else:
      return (porcen_vector(cdr(lista),n))


print(porcen_vector([3, 3, 3, 3 ,3 ,3 ,10 ,10,10 ,10],3))
print(porcen_vector([2, 2, 3, 4 ,5 ,6 ,10 ,10,10 ,10],1))
print(porcen_vector([1,2,3,4,5,6],4))


print("")
print("Pregunta 7 a")
def aplica_fun(fun ,lista):
  if(len(lista)== 0):
    return (0)
  
  else:
    return (list(fun(car(lista))),aplica_fun(fun,cdr(lista)))



print("Pregunta 7 b")

def ordena_lista(lista):
  if(len(lista) <= 1):
    return (lista)
  
  else:
    pivote = lista[1]
    del lista[0]
    lista_resto = lista
    return( list (ordena_lista(lista_resto[lista_resto<pivote]),
               pivote,
               ordena_lista(lista_resto[lista_resto>=pivote])))


#print(ordena_lista([16,4,12,13,3,8,88]))


print("")
print("Pregunta 7 c")


def pega_dos_listas(lista1,l2):
  
  if not lista1:
      return (l2)
  else:
    return cons(car(lista1),pega_dos_listas(cdr(lista1),l2))


def pega_tres_listas(lista1,lista2,lista3):
  return (pega_dos_listas(lista1,pega_dos_listas(lista2,lista3)))



l = pega_tres_listas([1,2],[3,4],[5,6])
print(l)
l = pega_tres_listas([1,2,2,2],[3,4],[5,6])
print(l)
l = pega_tres_listas([1,2,2,2],[3,4],[5,6,7,8,9])
print(l)


print("")
print("Pregunta 7 d")

def subconjunto(l1,l2):
    if not l1 :
        return True
    if not l2:
        return False
    if car(l1) == car(l2):
        return subconjunto(cdr(l1),cdr(l2))
    else:
        return subconjunto(l1 ,cdr (l2))
    
    
print(subconjunto([1,2,3],[5 ,1 ,2 ,8 ,7 ,3 ,9]))    
print(subconjunto([1,2,3],[5 ,1 ,8 ,7 ,3 ,9]))    
print(subconjunto([6 ,8, 7 ,1, 3 ,9],[5 ,1 ,3 ,9]))    

    
print("")
print("Pregunta 7 e")
    
def eliminar(n,lista):
    if n in lista:
        lista.remove(n)
        return lista
    return lista

print(eliminar(5,[ 9 ,8, 7, 6, 5, 4, 3, 2, 1]))
print(eliminar(1,[ 9 ,8, 7, 6, 5, 4, 3, 2, 1]))
print(eliminar(9,[ 9 ,8, 7, 6, 5, 4, 3, 2, 1]))

    
print(" ")  
print("Ejercicio 3 e")

def imprimecom(c):
    print("")
    print(""+str(parte_real(c))+" + "+str(parte_compleja(c))+"i")

    print("")


print(" ")  
print("Ejercicio 3 a")


def complejo (a, b ):
  return cons (a ,b)


def parte_real(c):
    return car(c)

def parte_compleja(c):
    return cdr(c)


def suma_com(c1,c2):
    return complejo( parte_real(c1)+ parte_real(c2),parte_compleja(c1) + parte_compleja(c2))

imprimecom(suma_com(complejo(4,8),complejo(-4,-10)))
imprimecom(suma_com(complejo(-4,12),complejo(-6,-12)))
imprimecom(suma_com(complejo(-4,0),complejo(-4,-12)))
print(" ")  
print("Ejercicio 3 b")
def res_com(a,b):
    return complejo(parte_real(a) - parte_real(b),parte_compleja(a)- parte_compleja(b))
imprimecom(res_com(complejo(4,8),complejo(-4,-10)))
imprimecom(res_com(complejo(-4,12),complejo(-6,-12)))
imprimecom(res_com(complejo(-4,0),complejo(-4,-12)))

print(" ")
print("Ejercicio 3 c")

def mul_com(a,b):
    return complejo(parte_real(a) * parte_real(b) - parte_compleja(a)*parte_compleja(b),
                    parte_real(a) * parte_compleja(b) + parte_compleja(a) * parte_real(b))


imprimecom(mul_com(complejo(4,8),complejo(-4,-10)))
imprimecom(mul_com(complejo(-4,12),complejo(-6,-12)))
imprimecom(mul_com(complejo(-4,0),complejo(-4,-12)))

print(" ")
print("Ejercicio 3 d")

def conjugado(a):
    return complejo(parte_real(a),-1 * parte_compleja(a))


imprimecom(conjugado(complejo(4,12)))
imprimecom(conjugado(complejo(-4,12)))
imprimecom(conjugado(complejo(-4,-12)))

print(" ")
print("Ejercicio 4")
def divisibles_iter(lista,x,si,no):
    if not lista :
        return cons(si,no)
    else:
        if (car(lista)%x) == 0:
            return divisibles_iter(cdr(lista),x,(cons(car(lista),si)),no)
        else:
            return divisibles_iter(cdr(lista),x,si,cons(car(lista),no))
        
    
def divisibles(lista,x): 
    return divisibles_iter(lista,x,list(),list())
    

print(divisibles([2,3,4,5,6,7,8,9],2))
print(divisibles([2,10,4,5,6,7,8,12],2))
print(divisibles([2,3,6,7,8,9],2))



print(" ")
print("Ejercicio 5")
def per(n,l):
    if not l:
        return False
    else:
        if n == car(l):
            return True
        else:
            return per(n,cdr(l))
        
        
        
print(per(1,[1,2,3,4,5,6]))
print(per(10,[1,2,3,4,5,6]))
print(per(6,[1,2,3,4,5,6]))


    

print(" ")
print("Ejercicio 5 b")

def restalistas(l1,l2):
    if not l1:
        return list()
    if per(car(l1),l2):
        return restalistas(cdr(l1),l2)
    return cons(car(l1), restalistas(cdr(l1),l2))
        

print(restalistas([7 ,1 ,4 ,3 ,2 ,4 ,2 ,4 ,6],[5,1,4]))
print(restalistas([7 ,1 ,4 ,3 ,2 ,4 ,2 ,4 ,6],[1 ,7, 3, 2]))
print(restalistas([7 ,1 ,4 ,3 ,2 ,4 ,2 ,4 ,6],[5,5,5,5]))


print("")
print("Ejercicio 6")

def pares(l1,l2):
    if len(l1) != len(l2):
        return list()
    if not l1:
        return list()
    else:
        return cons([car(l1),car(l2)],pares(cdr(l1),cdr(l2)))
        
print(pares([7,1,4,3],[5,1,4,-1]))
print(pares([7,1,4,3,1],[5,1,4,-9,0]))
print(pares([7,1],[5,0]))


print("")
print("Ejercicio 7")

def factores(n):
    return factores_fun(n,2)

def factores_fun(n,k):
    if k > n:
        return list()
    if (n%k) == 0:
        return cons(k,factores_fun((n/k),k))
    else:
        return factores_fun(n,k+1)


print(factores(60))
print(factores(30))
print(factores(135))


print(" ")
print("Ejercicio 8")

def es_menor(x,y):
    return x < y

def vuelto(n):
   return vuelto_iter(n , [200,100,50,25,10,5,1],list())

def vuelto_iter(x,l,r):
    if x <= 0 :
        return r
    else:
            if es_menor(x,car(l)):
                return vuelto_iter(x,cdr(l),r)
            else:
                return vuelto_iter(x-car(l),l,cons(car(l),r))




print(vuelto(555))
print(vuelto(758))
print(vuelto(1236))

