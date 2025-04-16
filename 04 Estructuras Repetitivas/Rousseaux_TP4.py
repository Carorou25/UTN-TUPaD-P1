# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100(incluyendo ambos extremos), 
# en orden creciente, mostrando un número por línea.

for i in range(0, 100):
    print(str(i) + " ", end="" )

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un número entero")) 
cont = 0 
while numero > 0 :
    cont = cont + 1 
    numero = numero // 10 
print("La cantidad de digitos del numero es:" , cont)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese un número entero")) 
valor2 = int(input("Ingrese otro número entero")) 
suma = 0
for i  in range (valor1 + 1 , valor2): 
    suma = suma + i 
print("La suma de los números es: ", suma)

# 4)Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero = int(input("Ingrese un número entero. Ingrese 0 para detener la operación"))
suma = 0 
acumulador = ""  
while numero != 0: 
    suma = suma + numero   
    acumulador =   acumulador + str(numero) + " "
    numero = int(input("Ingrese un número entero. Ingrese 0 para detener la operación"))
print("Los numeros sumados son: ", str(acumulador) , " " , end = " ")         
print(" \n La suma de los numeros es: ", suma)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, 
# el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random 

numero_aleatorio = random.randint(0,9)

cont = 0 

while True:
    numero = int(input("Adivina un número.")) 
    cont = cont + 1 
    if numero == numero_aleatorio: 
        print("Felicidades. Acertaste!")
        break
    else: 
        print("Intentalo de nuevo!") 
print("Hicieron falta ", cont, "intentos.") 

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100 ,-1, -2): 
    print(str(i), " ", end = " ") 


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un número positivo")) 
suma = 0
for i in range(0, num +1 ):
    suma = suma + i
print("La suma de los números es: ", suma )


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 


cantidad = 100 
positivo = 0
negativo = 0
par = 0
impar = 0
for i in range(cantidad): 
    numero = int(input("Ingrese números enteros. ")) 
    if numero % 2 == 0: 
        par = par + 1
    else: 
        impar = impar + 1
    if numero < 0: 
        negativo = negativo + 1
    else:
        positivo = positivo + 1

print("Hay ", par, "números pares.")
print("Hay ", impar, "números impares.")
print("Hay ", negativo, "números negativos.")  
print("Hay", positivo, "números positivos.")   

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

from statistics import  mean 

cantidad = 100 
numeros = []

for i in range(cantidad):
    numero = int(input("Ingrese números enteros")) 
    numeros.append(numero)
    media = mean(numeros) 
print("La media de los valores ingresados es: ", media)

# 10)Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número entero: "))
inverso = 0 
while numero != 0: 
    digito = numero % 10 
    inverso = inverso * 10 + digito
    numero = numero //10 
print("El número inverso es: ", inverso)     


