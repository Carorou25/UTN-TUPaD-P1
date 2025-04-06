#Ejercicio1

edad = int(input("Ingrese su edad: ")) 

if edad >= 18: 
    print("Es mayor de edad") 


#Ejercicio2

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado!")
else:
    print("Desaprobado!") 

#Ejercicio3

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0: 
    print("Usted ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")   


#Ejercicio4

edad = int(input("Ingrese su edad: "))

if edad < 12: 
    print("Es un niño/a") 

elif edad >=12 and edad < 18:
    print("Es un adolescente")
elif edad >= 18 and edad < 30: 
    print("Es un adulto/a joven")
else:
    print("Es un adulto")    

# Ejercicio5

contraseña = str(input("Ingrese una contraseña: "))
longitud = len(contraseña) 

if longitud >= 8 and longitud <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres.") 


#Ejercicio6

import random 

from statistics import mode, median, mean 

numeros_aleatorios = [random.randint(1,100) for i in range(20)] 

media = mean(numeros_aleatorios) 
mediana = median(numeros_aleatorios) 
moda = mode(numeros_aleatorios) 

print(numeros_aleatorios)
print(media)
print(mediana)
print(moda) 

if media > mediana and mediana > moda:
    print("Distribución con sesgo positivo.") 
elif media < mediana and mediana < moda:
    print("Distribución con sesgo negativo.") 
elif media == mediana == moda:
    print("Distribución sin sesgo.")
else: 
    print("No se puede determinar el sesgo")    


#Ejercicio7

palabra = str(input("Ingrese una palabra")) 

if palabra.lower().endswith(('a','e','i','o''u')):   #En este caso utilice la funcion endswith para poder determinar si termina en vocal la palabra. 
    palabra += '!'
    print(palabra)
else:
    print(palabra)         


#Ejercicio8

nombre = str(input("Ingrese su nombre: "))


def menu():    # Utilizo la funcion def en este caso para crear un menu de opciones. Y en funcion de la opcion seleccionada, se va desarrollando la estructura condicional. 

    print("Menú")
    print("1. Nombre en mayúsculas. ")
    print("2. Nombre en minúsculas")
    print("3. Nombre con primera letra en mayúscula")

menu()
opcion = input("Seleccionar una opción:")    

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower()) 
elif opcion == "3": 
    print(nombre.title()) 
else:
    print("Ingrese una opción válida") 



#Ejercicio9

magnitud = float(input("Ingrese la magnitud del terremoto.")) 

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4: 
    print("Leve (ligeramente perceptible)") 
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)") 
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7: 
    print("Muy fuerte (puede causar daños significativos)") 
elif magnitud >= 7:
    print("Extremo (puede causar daños a gran escala)")  
else:
    print("Datos incorrectos, ingrese un valor nuevamente")         



#Ejercicio10

hemisferio = str(input("Ingrese en que hemisferio se encuentra (N/S)")).upper()
mes = str(input("Ingrese mes del año: ")).lower()
dia = int(input("Ingrese dia del mes: ")) 


if hemisferio == 'S': 
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero" ) or (mes == "marzo"and dia <= 20):
        print("Es verano en el hemisferio sur")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes =="junio" and dia <= 20):       
        print("Es otoño en el hemisferio sur") 
    elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20): 
        print("Es invierno en el hemisferio sur") 
    elif (mes == "septiembre" and dia >= 21) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia <= 20): 
        print("Es primavera en el hemisferio sur") 
    else:
        print("Fecha no válida.")    
elif hemisferio == 'N': 
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero" ) or (mes == "marzo"and dia <= 20):
        print("Es invierno en el hemisferio norte")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes =="junio" and dia <= 20):       
        print("Es primavera en el hemisferio norte") 
    elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20): 
        print("Es verano en el hemisferio norte") 
    elif (mes == "septiembre" and dia >= 21) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia <= 20): 
        print("Es otoño en el hemisferio norte") 
    else:
        print("Fecha no válida.")  
else: 
    print("Error, hemisferio no válido. Ingrese los datos nuevamente.")     