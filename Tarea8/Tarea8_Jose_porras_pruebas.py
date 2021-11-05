import Tarea8_Jose_Porras_modulo as ldr


print("Pregunta 1")

print(ldr.pregunta1())

print("Pregunta 2")
print(ldr.pregunta2())

print("Pregunta 3")

print(ldr.pregunta3("The","Rolling","Stones"))

print("Pregunta 4")
print(ldr.isograma("isOgrAma"))

print("Pregunta 5")
print(ldr.esprimo(999331))

print("Pregunta 6")
print(ldr.smallprime([2,3,5,7,11,13,17,19]))

print("Pregunta 7")
print(ldr.pregunta7("Vocales"))

print("Pregunta 8")
print(ldr.pregunta8([1,2,3,4,5,2,3,4,5,5,5,6],2))

print("Pregunta 9")
print(ldr.pregunta9(12))

print("Pregunta 10")
print(ldr.diagonal([[15,25,-15],[-5,-122,85],[-56,666,322]]))

print("Pregunta 11")
dataclima = pandas.read_csv('clima.csv',sep=';',decimal=".")

print(ldr.estadisticasCol(dataclima,0))
print("Pregunta 12")
print(ldr.correlacionCols(dataclima, 4, 5))
