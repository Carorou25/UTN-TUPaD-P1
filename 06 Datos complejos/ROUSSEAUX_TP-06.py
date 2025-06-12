#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 


precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200 
precios_frutas['Manzana'] = 1500 
precios_frutas['Pera'] = 2300 

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800  

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200 
precios_frutas['Manzana'] = 1500 
precios_frutas['Pera'] = 2300  

precios_frutas['Banana'] = 1330 
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800 

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios.


precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 

agenda = {} 

for i in range(5): 
    numero_contacto = i + 1
    nombre = input(f"Ingrese el nombre del contacto {numero_contacto}: ") 
    telefono = input(f"Ingrese el número telefonico de {nombre}: ")
    agenda[nombre] = telefono 
print(agenda) 

consulta = input("Ingrese el nombre del contacto que desea consultar: ") 

if consulta in agenda: 
    print(f"El número de {consulta} es {agenda[consulta]}")
else: 
    print("Error. No se encontró el contacto") 

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra. 

frase = input("Ingrese una frase: ") #Solicito el ingreso de una frase

palabras = frase.split() #Separo las palabras con split 

# print(palabras)  

palabras_unicas = set(palabras) # saco las palabras repetidas creando un set

print(palabras_unicas) #Muestro las palabras sin repetir 

diccionario = {} 

for palabra in palabras: 
    if palabra in diccionario:
        diccionario[palabra] += 1 
    else: 
        diccionario[palabra] = 1

    
print(diccionario) 

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 

alumnos = {}

for i in range(3):
    nombre = input("Ingrese nombre del alumno: ") 
    notas = [] 
    for j in range(3): 
        nota = float(input(f"Ingresa la nota {j+1} de {nombre}: "))
        notas.append(nota) 
    alumnos[nombre] = tuple(notas) 

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}") 