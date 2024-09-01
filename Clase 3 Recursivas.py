#-------------------------------------------------------------------------------
# Name:        Clase 3
#
# Author:      Ariadna Villagra
#
# Created:     01/09/2024

#-------------------------------------------------------------------------------
#Ejercicio 1
def sumatotal():
 num = int(input("Ingrese un número"))
 suma = 0
 for i in range (0, num+1):
  suma += i
 return suma

resultado = sumatotal()

print("La suma total es:", resultado)
