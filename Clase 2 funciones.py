#-------------------------------------------------------------------------------
# Name:        Clase 2 Funciones
# Author:      Ariadna Villagra

#1. Realizar una función que se llame area_rectangulo() que devuelva el área del rectángulo a
#partir de su base y altura.
#2. Realizar una función que se llame relacion() que a partir de dos nros realice lo siguiente:
#a. Si el primer nro es mayor que el segundo, devuelve 1
#b. Si el primer nro es menor que el segundo, devuelve -1
#c. Si ambos nros son iguales, devuelve 0
#3. Realizar una función que se llame intermedio() que a partir de dos nros devuelva el punto
#intermedio. Ej. El punto intermedio entre 10 y 24 = 17; entre 12 y 50 = 31.
#4. Realizar una función que se llame separar() que reciba una lista de nros y devuelva dos listas
#ordenadas. La primera con nros pares y la segunda con nros impares.
#5. Cada punto debe estar en un commit diferente subido al repositorio remoto.

#-------------------------------------------------------------------------------

#Ejercicio 1

def area_rectangulo(altura, base):
    # Instrucción 1
    area = altura * base

    return area

print (area_rectangulo(5, 4))

#Ejercicio 2
def relacion(num1, num2):
    # Instrucción 1
    if (num1 < num2):
       return -1
    elif (num1 > num2):
       return 1

    else:
       return 0

print (relacion(2, 2))

#Ejercicio 3
def intermedio(num1, num2):
    # Instrucción 1
    suma = num1 + num2
    inter = suma / 2
    return inter

print (intermedio(10, 24))


#Ejercicio 4
def separar(lista):
    # Instrucción 1

  lista1 = []
  lista2 = []
  i = 0
  for numero in lista:


     if (numero % 2 == 0 ):
         lista1.append(numero)

     else:
         lista2.append(numero)

  return lista1,lista2

print(separar([1,2,4]))
