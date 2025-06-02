
# 1) Crea una función recursiva que calcule el factorial de un número. 
#Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

#Definición de funciones
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1) 

#Programa principal 

numero = int(input("Ingresa un número positivo")) 
print(f"El factorial del número ingresado es: {factorial(numero)}") 



# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, 
# muestra la serie completa hasta la posición que el usuario especifique. 

#Definición de funciones 

def fibonacci_recursivo(posicion):
    if posicion == 0: 
        return 0 
    elif posicion == 1:
        return 1 
    else: 
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

#Programa principal     

posicion = int(input("Ingresa un número positivo: "))
print(f"El valor de la serie Fibonacci en la posición ingresada es: {fibonacci_recursivo(posicion)}") 


## 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛**𝑚= 𝑛*𝑛**(𝑚−1). Prueba esta función en un algoritmo general. 

def potencia_recursiva(base, exponente): 
    if exponente == 0:
        return 1  
    else: 
        return base * potencia_recursiva(base, exponente - 1)


base = int(input("Ingrese un número de base: "))
exponente = int(input("Ingrese un número de exponente: "))

print(f"El resultado de la potencia para los números ingresados es:  {potencia_recursiva(base,exponente)}")

# base = n
# exponente = m 

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto. 

#Definicion de funciones 

def binario_recursivo(num_decimal):  
    if num_decimal == 0:
        return "0"
    elif num_decimal == 1: 
        return "1" 
    else: 
        return binario_recursivo(num_decimal//2) + str(num_decimal % 2)    


#Programa principal 

num= int(input("Ingresa un número positivo: ")) 

print(f"El número decimal {num} en binario es : {binario_recursivo(num)}")  


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.

# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

#Definición de funciones 

def es_palindromo(palabra):   
    if len(palabra) == 0:
        return True  
    elif palabra[0] != palabra[-1]: 
        return False 
    else: 
        return es_palindromo(palabra[1:-1])


#Programa principal 

palabra = input("Ingresa una palabra: ").lower() 

print(es_palindromo(palabra)) 


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

#Definición de funciones 

def suma_digitos(num):
    if num < 10:
        return num
    else: 
          return  suma_digitos(num // 10) + (num % 10)



#Programa principal 

num = int(input("Ingresa un número entero: "))

print(f"La suma de los dígitos del número {num} es: {suma_digitos(num)}")  


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de 
# bloques que necesita para construir toda la pirámide. 

#Definición de funciones 

def contar_bloques(n): 
    if n == 1: 
        return 1 
    else: 
        return n + contar_bloques(n - 1) 
    
#Programa principal 

n = int(input("¿Cuántos bloques hay en el nivel más bajo?")) 
print(f"La cantidad de bloques necesarios para construir la pirámide es: {contar_bloques(n)}")  

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
# y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número. 

#Definición de funciones 

def contar_digito(numero, digito):
    if digito == 0:
        return 0 
    elif digito == 0:
        return 0 
    else: 
        return 1 + contar_digito(numero // 10, digito)
        


#Programa principal 

numero = int(input("Ingresa un número psoitivo: "))
digito = int(input("Ingresa un dígito del 0 al 9: ")) 
print(f"La cantidad de veces que aparece el dígito {digito} en el número {numero} es: {contar_digito(numero, digito)}")   
