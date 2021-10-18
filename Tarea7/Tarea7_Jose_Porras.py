# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import statistics
import numpy
import pandas
r = abs((2-pow(5,4)*(12/5)*(-42-6*2)))
print(r)
r=math.factorial(6)
print(r)
r = math.log(12,2)
print(r)
r= math.log(54,10)
print(r)
r = pow(math.e,0.405022)
print(r)




#Pregunta 2
print("Pregunta 2")
x = -76
y = 2*math.pi + 1
z = (math.sqrt(12*pow(y,3)+4*pow(x,2)))/4*y
print(z)
#Pregunta 3
print("Pregunta 3")

print("Par" if 21%2 == 0 else "Impar")
print("Par" if 134%2 == 0 else "Impar")
print("Par" if 89%2 == 0 else "Impar")

print("Pregunta 4")

def diaSemana(num):
    if num > 7 or num < 1 :
        print("El numero debe estar entre 1 y 7")
    elif num == 1:
        print("Hoy es domingo")
    elif num == 2:
        print("Hoy es lunes")
    elif num == 3:
        print("Hoy es martes")
    elif num == 4:
        print("Hoy es miercoles")
    elif num == 5:
        print("Hoy es jueves")
    elif num == 6:
        print("Hoy es viernes")
    elif num == 7:
        print("Hoy es sabado")
        
        

diaSemana(4)        
diaSemana(2)        
diaSemana(9)        


print("Pregunta 5")

def solCuadratica(a,b,c):
    if not a:
        print("Ecuacion degenerada")
    else:
        discriminante =pow(b,2)+4*a*c
        if discriminante < 0:
            print("La ecuacion no posee soluciones reales")
        elif not discriminante:
             print("La ecuacion posee una solucion")
             print("Sol: ",(-b+math.sqrt((-pow(b,2))+4*a*c))/2*a)
        elif discriminante > 0:
            
            print("La ecuacion posee dos soluciones")
            discriminanteP = (-b+math.sqrt((-pow(b,2))+4*a*c))/2*a
            disriminanteN = (-b-math.sqrt((-pow(b,2))+4*a*c))/2*a
            print("Soluciones: "+ str(discriminanteP) + " " + str(disriminanteN))
            

solCuadratica(9, 0, 2) 
solCuadratica(0, -2, 3) 
solCuadratica(2, -4, 2) 
        

print("")
print("Pregunta 6")

vec = [81, 35, 72, 50, 67, 8, 101, 22, 96, 13]

print("Media :",statistics.harmonic_mean(vec))
print("Varianza: ",statistics.variance(vec))
print("Desviacion Estandar: ",statistics.stdev(vec))
print("Ultimos 4: ",vec[-4:])
print("Maximo: ",max(vec)) 
print("Suma del vector: ",sum(vec))
vecInv = vec.reverse()
print("Lista invertida: ",vec)


print("")
print("Pregunta 7")


matriz1= numpy.array([[-7,1,6],[12,9,3]])
matriz2= numpy.array([[-10,-1],[3,-12],[-5,5]])

print("Operacion de matriz")
print(numpy.add(matriz1,numpy.multiply(34,matriz2.T)))
print("")
print("Pregunta 8")

matrizA = numpy.array([[6,7,-5],[1,-8,-6],[10,13,4]])

print("Suma diagonal: ", numpy.trace(matrizA))

print(" ")
print("Pregunta 9")


datanotas = {'Nombre':['Lucia','Pedro','Ines','Luis','Andres','Ana'],
             'Matematicas':[7,7.5,7.6,5,6,7.8],
             'Ciencias':[6.5,9.4,9.2,6.5,6.0,9.6],
             'Español':[9.2,7.3,8.0,6.5,8.7,7.7],
             'Historia':[8.6,7,8,7,8.9,8],
             'EdFisica':[8,7,7.5,9,7.3,6.5],
             'Genero':['F','M','F','M','M','F']}

dataframenotas = pandas.DataFrame(datanotas)

print(dataframenotas)    
print(" ")   
print("Pregunta 10")
print("Info:")
print(dataframenotas.info())
print("")
print("Columas")
print(dataframenotas[['Nombre','Matematicas','Ciencias']])
print(" ")
print("Iloc")
print(dataframenotas.iloc[:])
print(" ")
print("Loc")
print(dataframenotas.loc[:])
print("")
print("Correlacion Ciencias-Español")   
print(numpy.correlate(numpy.ravel(dataframenotas[["Ciencias"]]),numpy.ravel(dataframenotas[["Español"]])))
size = numpy.ravel(dataframenotas[["Ciencias"]])

print(" ")
print("Pregunta 11")    

dfheart = pandas.read_csv('SAheart.csv',sep=';')
print(dfheart)
print("Dimension")
print(dfheart.shape)
print("")
#print(dfheart.loc[:]) 
def sum_cuan(dataf):
    total = 0
    for colum in dataf:
        if dataf[colum].dtypes != 'object':
            total = total + dataf[colum].sum()
    return total        
        
    

print("Suma variables cuantitativas",sum_cuan(dfheart))
 
def moda(dataf):
    modas =[]
    for col in dataf:
        if dataf[col].dtypes == 'object':
            modas.append(statistics.mode(dataf[col]))
    return modas

print(" ")        
print("Modas de variables cualitativas")
print(moda(dfheart))

print("")
def dic(dataf):
    resumen = {}
    resumen['Media'] = statistics.harmonic_mean(dataf['obesity'])
    resumen['Moda'] = statistics.mode(dataf['obesity'])
    resumen['Maximo'] = max(dataf['obesity'])
    resumen['Minimo'] = min(dataf['obesity'])
    return resumen


print(" ")
print("Diccionario de datos")
print(dic(dfheart))
#print(dfheart['obesity'])


def termina4():
    for n in range(100):
        if n%10 == 4:
            print(n)
            
print("")
print("Pregunta 12")
termina4()
            
            
        