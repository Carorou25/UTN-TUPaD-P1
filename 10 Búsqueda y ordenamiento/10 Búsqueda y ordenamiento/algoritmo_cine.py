# En este algoritmo vamos a trabajar con una lista de butacas de cine, para ver si estan vacías u ocupadas

# Definimos la función para la busqueda binaria 
def busqueda_binaria(butacas_ocupadas,consulta): #Defino función con parámetros
    izquierda = 0              #Posicion 0 de la lista 
    derecha = len(butacas_ocupadas) - 1      #Ultima posicion de la lista (longitud de nuestra lista - 1)
    
    while izquierda <= derecha:    #Mientras se cumpla la condicion de busqueda en ese rango
        medio = (izquierda + derecha) // 2         #Buscamos el punto medio de la lista ordenada 
        
        if butacas_ocupadas[medio] == consulta:  #Comparo el índice medio con el valor de consulta 
            return medio                        #Si es igual, retorno ese valor 
        elif butacas_ocupadas[medio] < consulta:   #Si el valor medio es menor del valor que queremos buscar 
            izquierda = medio + 1                #Se actualizan las variables de izquierda y derecha 
        else:                                    # Y se actualiza el índice 
            derecha = medio - 1
    
    return None  

# Programa principal 

#Creamos una lista 
butacas_ocupadas = []  
for i in range(1,51,5): 
    butacas_ocupadas.append(i) 

#Hacemos la consulta de la butaca 
consulta = int(input("Ingrese el número de butaca que desea consultar: "))

#Mostramos por pantalla 
print("El número de butacas ocupadas es: ", butacas_ocupadas)

resultado = busqueda_binaria(butacas_ocupadas, consulta)

if resultado != None:  #Se evalúa si la butaca está libre u ocupada. 
    print(f"La butaca {consulta} está ocupada.") 
else: 
    print(f"La butaca {consulta} está libre.") 

















