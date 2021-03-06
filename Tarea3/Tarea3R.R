install.packages("knitr",dependencies = T)
install.packages("rmarkdown", dependencies = T)

#Tarea 3 R Jose Andres Porras Mu�oz
#Paradigmas de Programacion

#Pregunta 1a
vector.x <- c(7,-5,31,-2,-9,10,0,18)
vector.y <- c(2,2,-3,1,99,-10,10,-7)

#Pregunta 1b
mean(vector.x)
var(vector.x)
sqrt(vector.x[vector.x>0])
sd(vector.x)

#Pregunta 1c
mean(vector.y)
var(vector.y)
sqrt(vector.y[vector.y>0])
sd(vector.y)



#Pregunta 1d
cor(vector.x,vector.y)

#Pregunta 1e
vector.x[2:7]

#Pregunta 1f
vector.y[-c(2,7)]

#Pregunta1g
vector.y[vector.y < -3 | vector.y > 10]
#Pregunta 1h

vector.x[vector.x > 0 & ((vector.x %% 2) == 0)]


#Pregunta 2
A = matrix(c(1,2,3,4,5,6,7,8,9,10,11,12),nrow=4,"byrow"="true")
A
#Explicaciones


#Lee la primera fila y de la columna 1 a 3
A[1,1:3]

#Lee de la fila 1 a la 4 y solo la columna 2
A[1:4,2]


#Lee la fila y columna 3
A[3,3]

#Lee el elemento 11 leyendo por columnas y 
#de manera descendente
A[11]

#Lee el elemento 20 pero no existe
A[20]

#Lee la fila 5 que no existe y la columna 4
#A[5,4]

#Lee el elemento 1,1,1 de una matriz de 3 dimensiones, da error porque la matriz es de 2 dimensiones

#A[1,1,1]

#Pregunta 3

# as.matrix(x) intenta convertir el parametro en una matriz 

mi_vector <- c("a", "b", "c")
as.matrix(mi_vector)

# as.data.frame(x) intenta convertir el parametro en un data frame tratando de conservar los datos, nombres
# de columnas entre otros
mi_matriz <- matrix(1:4, nrow = 2)

as.data.frame(mi_matriz)

#Pregunta 4

nivel.educ <- factor(c("Lic","Bach","Bach","Bach","Dr","MSc"),
                     levels = c ("Lic","Bach","Dr","MSc"))

datos <- data.frame(Peso = c(56,67,55,57,87,48), Edad = c(28,23,19,18,57,13), "Nivel Educativo" = nivel.educ)

datos


#Pregunta 5

vector.z <- c(2,-5,4,6,-2,8)
vector.z

vector.a <- vector.z[vector.z>0]
vector.a

vector.b <- vector.z[vector.z<0]
vector.b

vector.c <- vector.z[-1]
vector.c

vector.d <- vector.z[c(T,F)]
vector.d


#Pregunta 6

setwd("C:/Users/Andr�s/Porras/UNIVERSIDAD NACIONAL/Carrera/Paradigmas Programacion/Tareas/Tarea3")
datos.portabilidad <- read.table('potabilidad_V2.csv',
                    header=TRUE, sep=',',dec='.',row.names=1)

dim(datos.portabilidad)

datos.portabilidad[,c(1,2)]

summary(datos.portabilidad)

str(datos.portabilidad)

mean(datos.portabilidad[,1])

mean(datos.portabilidad[,2])

sd(datos.portabilidad[,1])

sd(datos.portabilidad[,2])


#al leer el archivo con sep=';' los datos se agrupan de manera incorrecta y a
#la hora de leer el data frame no puede leer los numeros de manera correcta


#Pregunta 7
datos.aheart <- read.table('SAheart.csv',
                                 header=TRUE, sep=';',dec='.',row.names=NULL)

dim(datos.aheart)

datos.aheart [,c(1,3)]

summary(datos.aheart )

str(datos.aheart )

cor(datos.aheart[,2], datos.aheart[,8])


colSums(datos.aheart[-c(5,10)])

#### Sbp

min(datos.aheart[,1])
max(datos.aheart[,1])

#### Tobacco
min(datos.aheart[,2])
max(datos.aheart[,2])


#### ldl
min(datos.aheart[,3])
max(datos.aheart[,3])


#### adiposity
min(datos.aheart[,4])
max(datos.aheart[,4])

#### Typea
min(datos.aheart[,6])
max(datos.aheart[,6])


#### Obesity
min(datos.aheart[,7])
max(datos.aheart[,7])


#### Alcohol
min(datos.aheart[,8])
max(datos.aheart[,8])

#### Age

min(datos.aheart[,9])
max(datos.aheart[,9])


###Mediana y Media de variables cuantitvas
apply(datos.aheart[,c(1,2,3,4,6,7,8,9)],2,median)

colMeans(datos.aheart[,c(1,2,3,4,6,7,8,9)])



#### Chd

sum(datos.aheart[,10]=="Si")

sum(datos.aheart[,10]=="No")




#Pregunta 8

num.aleatorios <- function(){
  random.numbers <- sample(1:500, 200)
  random.vector<- random.numbers[random.numbers >= 50 | random.numbers <= 450]
  return (length(random.vector))
}

num.aleatorios()
num.aleatorios()
num.aleatorios()

#Pregunta 9
costo.llamada <- function(t){
  if(t<1){
    return (0.4)
  }
  else{
    return (0.4 + (t - 1)/4)
  }
}


costo.llamada(1)
costo.llamada(2)
costo.llamada(7)

#Pregunta 10
calc.traza<- function(matriz){
  if(nrow(matriz) ==  ncol(matriz)){
    return (sum(diag(matriz)))
  }
  return (0)
  
}

calc.traza(matrix(c(9,30,4,1,30,-1,4,12,-2),nrow=3))
calc.traza(matrix(c(9,8,4,1,30,-8,4,12,-2,4,8,10,99,0,5,-10),nrow=4))
calc.traza(matrix(c(9,-3,4,1,15,-8,4,12,-2,8,1,9,5,6),nrow=2))

#Pregunta  11
fibonacci.n <-function(n){
  contador = 2;
  n1 = 0
  n2 = 1
  if(n == 1) {
    print("Fibonacci:")
    print(n1)
  }
  else{
    print("Fibonacci:")
    print(n1)
    print(n2)
    while(contador < n) {
      n3 = n1 + n2
      print(n3)
      # update values
      n1 = n2
      n2 = n3
      contador = contador + 1
    }
  }
  
}

fibonacci.n(7)
fibonacci.n(1)
fibonacci.n(12)


#Pregunta 12
entero.mayor <- function(x){
  numero = 0
  while( (numero*numero) < x){
    numero = numero + 1
  }
  return (numero-1)
}


entero.mayor(12)
entero.mayor(100)
entero.mayor(1)

#Pregunta 13

nombres <- c("Jose","Andres","Pablo","Joaquin","Oscar","Yeikol","Steve","Alex","Agnes","Willy")
datos.alumnos = data.frame(Edad = sample(12:21, 10),A�o.de.Nacimiento =sample(2000:2009, 10),
                           Tel�fono = sample(10000000:99999999,10))
row.names(datos.alumnos) <- nombres
datos.alumnos



#Pregunta 14


divisible.3<-function(dataframe){
  cantidad = 0
  datafram1 = as.matrix(dataframe)
  for(i in 1:ncol(datafram1)) { 
    if(( datafram1[ i, i]%% 3) == 0){
        cantidad = cantidad + 1
    }
  }
  return (cantidad)
}

df = data.frame(replicate(3,sample(0:999,3,rep=TRUE)))
df
divisible.3(df)
df1 = data.frame(replicate(3,sample(0:999,3,rep=TRUE)))
df1
divisible.3(df1)
df2 = data.frame(replicate(3,sample(0:999,3,rep=TRUE)))
df2
divisible.3(df2)
#Pregunta 15

output.data <- function(dataframe,col1,col2){
  lista <- list(columna1 = colnames(dataframe[col1]),columna2 = colnames(dataframe[col2]),
                correlacion = cor(dataframe[col1],dataframe[col2]), covarianza = cov(dataframe[col1],dataframe[col2]) 
                )
  return (lista)
}




output.data(data.frame(replicate(3,sample(0:999,3,rep=TRUE))),1,2)
output.data(data.frame(replicate(3,sample(0:999,3,rep=TRUE))),1,3)
output.data(data.frame(replicate(3,sample(0:999,3,rep=TRUE))),2,3)
#Pregunta 16

U <- function(n){
  if(n==0) {
    return(5)
  }
  else {
    if(n==1) {
      return(-5)
    }
    else {
      if(n == 2){
        return (2)
      }
      else{
      return(U(n-1)-11*U(n-2)+2*U(n-3))
        
      }
    }
  }
}


U(5)
U(2)
U(9)
#Pregunta 17


collatz <- function(n) {
  # n is the initial number
  if(n == 1){
    return (0)
  }
  else{
    if (n %% 2 == 0) {
      return ((collatz(n/2)) + 1)
    } else {
      return ((collatz(3*n + 1)) + 1)
    }
  }
}

collatz(16)
collatz(12)
collatz(31)



# Pregunta 18

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


clasificacion(6)
clasificacion(47)
clasificacion(12)





