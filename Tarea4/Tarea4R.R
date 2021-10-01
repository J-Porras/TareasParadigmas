install.packages("lisp")
library(lisp)

#Tarea 3 R (Tarea 1 y 2 de LISP) Jose Andres Porras Muñoz
#Paradigmas de Programacion

#Pregunta 1
ackerman <- function(n,m){
  if(m == 0){
    return (0)
  }
  if(n == 0){
    return (2 * m)
  }
  if(m == 1){
    return (2)
  }
  else{
    return (ackerman (n - 1, ackerman (n, m - 1)))
  }
}

ackerman(1,10)
ackerman(1,2)
ackerman(1,5)

#Pregunta 2
#Pregunta 2 Recursivo
collatz <- function(n){
  if(n == 1){return (0)}
  if((n%%2) == 0){return (1 + collatz(n/2))}
  else {return (1 + collatz(1 + (3 * n)))}
}

collatz(16)
collatz(8)
collatz(10)

#Pregunta 2 Iterativo

iter.collatz <- function(n,i){
  if(n == 1){return (0)}
  if((n%%2) == 0){return (iter.collatz((i + 1) ,(n/2)))}
  else {return (iter.collatz ((i+1),(1 + (3*n)) ))}
  
}

iter.collatz.wrapper <- function(n) {
  return (iter.collatz(n,0))
}
iter.collatz.wrapper(16)
iter.collatz.wrapper(8)
iter.collatz.wrapper(10)
#Pregunta 3
#Pregunta 3 Recursivo
pregunta.3 <-function(n){
  if(n == 0){return (1)}
  if(n == 1){return (0)}
  if(n == 2){return (-1)}
  else{return (2 * pregunta.3(n-1) - 7*pregunta.3(n-2) - 6 * pregunta.3(n-3))}
}

pregunta.3(4)
pregunta.3(12)
pregunta.3(13)

#Pregunta 3 Iterativo

pregunta.3.iter.wrapper<-function(n){
  pregunta.3.iter(0, -1, 1, 1,n)
}


pregunta.3.iter <- function(ant, res, transante, i, n){
  if(i >= n){
    return (ant)
  }
  else{
    return (pregunta.3.iter (res,((2*res) - (7*ant) - (6*transante)),ant,(i+1),n ))
  }
}

pregunta.3.iter.wrapper(4)
pregunta.3.iter.wrapper(12)
pregunta.3.iter.wrapper(13)
#Pregunta 4

#Pregunta 4 Normal


productoria.normal <- function(a, n){
  if(a  > n){
    return (1)
  }
  else{
    return ((((7 * a) + ( a* a* a) - 11)  *  ((7 * a) + ( a* a* a) - 11) ) * (productoria.normal ((a + 1),n )))
  }
}

productoria.normal(1,2)
productoria.normal(1,5)
productoria.normal(4,7)

#Pregunta 4 Termino



cuadrado<-function(a){
  return(a*a)
}
cubo<-function(a){
  return(a*a*a)
}
productoria<-function(f,a,n){
  if(a>n){
    return (1)
  }else{
    return(f(a)*productoria(f,(a+1),n))
  }
}

termino <-function(n){
  return (cuadrado(cubo(n)+(7*n)-11))
}

productoria.termino <-function(a, n){
  return (productoria(termino(n),a,n))
}

productoria.termino(1,2)
productoria.termino(1,5)
productoria.termino(4,7)
#Productoria 4 Lambda
productoria.lambda<-function(a,n){
  return (productoria((function(x) {cuadrado(cubo(x)+(7*x)-11)}),a,n))
}

productoria.lambda(1,2)
productoria.lambda(1,5)
productoria.lambda(4,7)

#Pregunta 5


es.factor <- function(x, k){
  if((x %% k) == 0){
    return (TRUE)
  }
  return (FALSE)
  
}



suma.factores <- function(x,k){
  if(k > ((x/2)+1)){
    return (0)
  }
  else{
    if(es.factor(x,k)){
      return (k + suma.factores(x,(k+1)))
    }
    else{
      return (suma.factores(x,(k+1)))
      
    }
  }
}

clasificacion <- function(n){
  if(suma.factores(n,1) == n){
    cat("Perfecto")
  }
  else{
    if(suma.factores(n,1) > n){
      cat("Abundante")
    }
    else{
      cat("Defectivo")
    }
  }
}


#Pregunta 6


porcen.vector <-function(lista, n){
  if(length(lista) == 0){
    return (0)
  }
  else{
    if(car(lista) <= n){
      return(1 + porcen.vector(cdr(lista),n ) )
    }
    else{
      return (porcen.vector(cdr(lista),n))
    }
  }
  
}




#Pregunta 7a

aplica.fun <- function(fun ,lista){
  if(length(lista)== 0){
    return (0);
  }
  else{
    return (c(list(fun(car(lista)))),aplica.fun(fun,cdr(lista)))
  }
}

#Pregunta 7b

ordena.lista<-function(lista){
  if(length(lista) <= 1){
    return (lista)
  }
  else{
    pivote <- lista[1]
    lista.resto <- lista[-1]
    return( c (ordena.lista(lista.resto[lista.resto<pivote]),
               pivote,
               ordena.lista(lista.resto[lista.resto>=pivote])))

      
  }
}
ordena.lista(c(16,4,12,13,3,8,88))
ordena.lista(c(1,2,3,4,5,6))
ordena.lista(c(6,5,4,3,2,1))
#Ejercicio 7c
pega.dos.listas <-function(lista1,l2){
  
  if(length(lista1) == 0){return (l2)}
  else{
    return (  c(lista1,l2) )
  }
}

pega.tres.listas <-function(lista1,lista2,lista3){
  return (pega.dos.listas(lista1,pega.dos.listas(lista2,lista3)))
}
z <- c(1,2)
x<-c(3,4)



pega.tres.listas(c(1,2),c(3,4),c(5,6))


#Ejercicio 7 d


subconjunto <- function(lista1,lista2,lista2or){
  if(length(lista1) == 0){
      return (T)
  }
  if(length(lista1) == 1 & length(lista2) == 1 & car(lista1) != car(lista2)){
    return (F)
  }
  if(car(lista1) == car(lista2)){
    return (subconjunto(cdr(lista1),lista2or,lista2or))
  }
  return (subconjunto (lista1,cdr(lista2),lista2or))
  
  
}
subconjunto.wrapper<-function(lista1,lista2){
  return (subconjunto(lista1,lista2,lista2))
}
subconjunto.wrapper(c(1,2),c(1,4,5,6,7,2))
subconjunto.wrapper(c(10),c(1,4,5,6,7,2))
subconjunto.wrapper(c(1,4,5,6,7,2),c(2,7,6,5,4,1))

#Pregunta 7 e

eliminar <- function(x,lst){
 if(length(lst) == 0){
   return (c())
 }
 if(x == car(lst)){
   return (cdr(lst))
 }
  else{
    return (c(car(lst),eliminar(x,cdr(lst))))
  }
}

eliminar(2,c(1,2,3,4,5))
eliminar(8,c(1,2,3,4,5))



#Pregunta 8

#Pregunta 8 e

output.complejo <- function(n) {
  cat(parte.real(n))
  cat(" + ")
  cat(parte.compleja(n))
  cat("i")
}

num.complejo <- function(a,b){
  return (c(a,b))
}

parte.real<-function(numero){
  return (car(numero))
}

parte.compleja <- function(numero) {
  return (cdr(numero))
  
}

#Pregunta 8 a

suma.complejo <- function(n1,n2) {
  return ( num.complejo( (parte.real(n1)+parte.real(n2)),(parte.compleja(n1)+parte.compleja(n2))))
}

output.complejo(suma.complejo(num.complejo(1,5),num.complejo(8,7)))
output.complejo(suma.complejo(num.complejo(10,-9),num.complejo(4,8)))
output.complejo(suma.complejo(num.complejo(-3,8),num.complejo(15,-7)))
#Pregunta 8 b

resta.compleja <-function(n1,n2){
  return ( num.complejo((parte.real(n1)-parte.real(n2)),(parte.compleja(n1)-parte.compleja(n2))))
}

#Pregunta 8 c

multi.compleja <- function(n1,n2){
  return (num.complejo ((parte.real(n1)*parte.compleja(n2))-(parte.compleja(n1)*parte.real(n2))
    ,(parte.real(n1)*parte.compleja(n2))+(parte.compleja(n1)*parte.real(n2))))
}


#Pregunta 8 d


conjugado.complejo<-function(n1){
  return(num.complejo(parte.real(n1),(-1 * parte.compleja(n1))))
}



#Pregunta 9



divisibles.iter<-function(lst, x, si, no){
  if(length(lst) == 0){
    return (c(si,no))
  }
  else{
    if( (car(lst)%%x) == 0){
      return (divisibles.iter(cdr(lst),x,c(list(c(car(lst),si))),no))
      
    }
    else{
      return (divisibles.iter(cdr(lst),x,si,c(list(c(car(lst),no)))))
      
      
    }
  }
}

divisibles <- function(lst, x) {
  return (divisibles.iter(lst,x,c(),c()))
}

divisibles(c(2,3,4,5,6,7,8,9),2)


#Pregunta 10

pertenece <- function(x,lst) {
  if(length(lst) == 0){return (F)}
  if(x == car(lst)){
    return (T)
  }
  else{
    return (pertenece(x ,cdr(lst)))
  }
}

resta.listas <- function(lst1,lst2) {
  if(length(lst1) == 0) {return(c()) }
  if(pertenece(car(lst1),lst2) == T){
    return (resta.listas(cdr(lst1),lst2))
  }
  return(c(car(lst1),resta.listas(cdr(lst1),lst2)))
  
}


resta.listas(c(7, 1, 4, 3, 2, 4, 2, 4, 6),c(5, 1, 4))

#Pregunta 11


crea.pares <- function(l1, l2) {
  if (length(l1) == 0) {
    return (NULL)
  }
  else{
    return (c(list(c(car(l1),car(l2))),crea.pares(cdr(l1),cdr(l2))))
  }
}


crea.pares(c(7,1,4,3),c(5,1,4,-1))



#Pregunta 12

factor <- function(n, k = 2) {
  if(k > n){
    return (c())
  }
  if((n%%k)==0){
    return ( c(list(c(k)),factor((n/k),k))  )
  }
  return (factor(n, (k+1)))
}

factor(60)

#Pregunta 13



vuelto.iter <- function(x, lst,r) {
  if((x<=0)){
    return (r)
  }
  else{
    if(x<car(lst)){
      return(vuelto.iter(x,cdr(lst),r))
    }
    else{
      return(vuelto.iter((x-car(lst)),lst,c(car(lst),r)))
    }
  }
}

vuelto <- function(x) {
  return(vuelto.iter( x,c(500,100,50,25,10,5,1),c() ))
}

vuelto(1325)














