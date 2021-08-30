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



#calcular la correlacion

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
A[5,4]

#Lee el elemento 1,1,1 de una amtriz de 3 dimensiones

A[1,1,1]

#Pregunta 3


#Pregunta 4

nivel.educ <- factor(c("Lic","Bach","Bach","Bach","Dr","MSc"),
                     levels = c ("Lic","Bach","Dr","MSc"))

datos <- data.frame(Peso = c(56,67,55,57,87,48), Edad = c(28,23,19,18,57,13), "Nivel Educativo" = nivel.educ)

datos


#Pregunta 5

vector.z <- c(2,-5,4,6,-2,8)

vector.a <- vector.z[vector.z>0]
vector.a

vector.b <- vector.z[vector.z<0]
vector.b

vector.c <- vector.z[-1]
vector.c

vector.d <- vector.z[c(T,F)]
vector.d


#Pregunta 6






