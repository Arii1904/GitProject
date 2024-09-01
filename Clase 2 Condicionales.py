#-------------------------------------------------------------------------------
# Name:        Clase 2
# Author:      Arita

#1. Pedir al usuario que ingrese un nro impar. Mientras que el usuario no ingrese un nro impar se
#volverá a pedir que ingrese un nro impar. Deberá indicar por pantalla si es impar.
#2. Pedir al usuario que ingrese dos nros. Luego imprimir 3 opciones (1. sumar, 2. restar y 3.
#multiplicar). Pedir al usuario que ingrese una opción, ejecutar la operación y mostrar por
#pantalla el resultado.
#3. Definir una lista de números y mostrar por pantalla el valor promedio. No utilizar funciones
#nativas sum() o len().
#4. Definir una lista de números, encontrar el valor mínimo de la lista e imprimirlo. No utilizar la
#función nativa min().
#5. Cada punto debe estar en un commit diferente subido al repositorio remoto.

#-------------------------------------------------------------------------------

#Ejercicio 1
nroimp = 2
nro = 2
resultado = nroimp % nro
while (resultado == 0):
    print (f'número {resultado}')
    nroimp = int(input("Ingrese nro impar"))
    resultado = nroimp % nro


print("Es impar")

#Ejercicio 2
primernro = int(input("Ingrese el primer numero "))
segundonro = int(input("Ingrese el segundo numero "))
sumar = primernro + segundonro
restar = primernro - segundonro
multiplicar = primernro * segundonro
opcion = int(input("Porfavor elija una opción 1. sumar, 2. restar y 3.multiplicar"))
if (opcion == 1):
   print(f'El resultado es : {sumar}')
elif (opcion == 2):
     print(f'El resultado es : {restar}')
else:
     print(f'El resultado es : {multiplicar}')
#Ejercicio 3
#lista de num
Listanum =[1,2,3]
sumatotal = 0
promedio = sumatotal / 3
for sumanum in Listanum:
 sumatotal += sumanum

promedio = sumatotal / 3
print("La promedio es = ",promedio)

#Ejercicio 4
#lista de num
Listanum =[1,2,3]
valormin = Listanum[0]

for num in Listanum:
    if num < valormin:
       valormin = num


print("El valor minimo es = ",valormin)
