
# 1) Crear una funcion llamada imprimir_hola_mundo que imprima por pantalla el mensaje:  "Hola Mundo!". Llamar a esta función desde el programa principal. 

#Definición de función 

def imprimir_hola_mundo(mensaje): 
    return mensaje

#Programa principal 

print(imprimir_hola_mundo("Hola Mundo!")) 

# 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. 
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devovler: "Hola Marcos!"
# Llamar a esta función desde el programa principal solicitando el nombre del usuario . 

#Definición de función 

def saludar_usuario(nombre):
    return (f"Hola {nombre}!")  #La función imprime éste mensaje cuando es llamada desde el programa principal 

#Programa principal 

nombre_usuario = input("¿Cómo te llamas?") 
print(saludar_usuario(nombre_usuario)) 

# 3) Crear una función llamada informacion_personal(nombre,apellido,edad,residencia)  que reciba cuatro parámetros e imprima: 
# "Soy {nombre} {apellido}, tengo {edad} años"
# y vivo en {residencia}". Pedir los datos al usuario y llamar a función con los valores ingresados. 

#Definir funciones 

def informacion_personal(nombre, apellido, edad, residencia):
    return  f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

#Programa principal 

mensaje1 = input("Ingresa tu nombre: ") 
mensaje2 = input("Ingresa tu apellido: ") 
mensaje3 = int(input("Ingresa tu edad: "))
mensaje4 = input("Ingresa tu residencia: ") 

print(informacion_personal(mensaje1, mensaje2, mensaje3, mensaje4)) 

# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados. 

import math

#Definir funciones 

def calcular_area_circulo(radio):
    return math.pi * radio ** 2 

def calcular_perimetro_circulo(radio): 
    return 2 * math.pi * radio

#Programa principal 

r = float(input("Ingrese el radio del círculo: ")) 
area = calcular_area_circulo(r) 
perimetro = calcular_perimetro_circulo(r)

print(f"El área del circulo es {area:.2f} y el perimetro es {perimetro:.2f}") 

#5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función. 

#Definición de funciones 

def segundos_a_horas(segundos): 
    return segundos/3600 

#Programa principal 

s= int(input("Ingrese los segundos: ")) 
horas = segundos_a_horas(s) 
print(f"{s} segundos corresponden a {horas:.2f} horas.") 

# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima la tabla de multiplicar de ese número del 1 al 10. 
# Pedir al usuario el número y llamar a la función. 

#Definición de funciones 

def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = i * numero 
        print(f"{numero} X {i} = {resultado}") 
    

#Programa principal

num = int(input("Ingresa un número entero: ")) 
tabla_multiplicar(num) 

# 7) Crear una función llamada operaciones_basicas(a,b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, 
# multilplicarlos y dividirlos. Mostrar los resultados de forma clara. 

#Definición de funciones 

def operaciones_basicas(a,b): 
    suma = a + b
    resta = a - b 
    multiplicacion = a * b 
    if b == 0:
        print("Indefinida. No es posible dividir por 0")
    else:
        division = a/b
    return (suma, resta, multiplicacion, division) 

#Programa principal 

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(num1,num2) 

print(f"Los resultados de las operaciones entre {num1} y {num2} son: ")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}") 
print(f"División: {resultados[3]:.2f}") 

# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en Kilogramos y la altura en metros, y devuelva el índice de masa corporal(IMC)
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales. 

#Definición de funciones 

def calcular_imc(peso,altura): 
    return peso/(altura**2)  

#Programa principal 

peso_en_kilogramos = float(input("Ingrese su peso en Kilogramos: "))
altura_en_metros = float(input("Ingrese su altura en metros: ")) 
resultado = calcular_imc(peso_en_kilogramos, altura_en_metros) 
print(f"Su índice de masa corporal es: {resultado:.2f}") 

# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente enFahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando  la función. 

#Definir funciones 

def celsius_a_fahrenheit(celsius): 
    return (9/5 * celsius) + 32 


#Programa principal 

temperatura = float(input("Ingrese la temperatura en Celsius: ")) 
resultado = celsius_a_fahrenheit(temperatura) 
print(f"El equivalente en fahrenheit de {temperatura} °C es: {resultado} °F")


# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

#Definición de funciones 

def calcular_promedio(a,b,c): 
    return (a + b + c)/3

#Programa principal 

num1 = float(input("Ingresa el primer número: ")) 
num2 = float(input("Ingresa el segundo número: ")) 
num3 = float(input("Ingresa el tercer número: ")) 
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los números ingresados es: {promedio:.2f}")  

