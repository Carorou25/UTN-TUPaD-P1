
#Creamos un diccionario con las ciudades y sus respectivas temperaturas 
meteorologia = [
                {"ciudad": "Rio Gallegos", "temperatura": 5}, 
                {"ciudad" :"Paraná", "temperatura": 9},  
                {"ciudad" : "Buenos Aires", "temperatura" : 10}
]

#Para buscar el dato, solicitamos el ingreso de un dato al usuario 

consulta = input("Ingrese la ciudad que desea consultar: ")

# Acá lo que hacemos es buscar en nuestros diccionarios si está el dato ingresado por el usuario. 
# Si está la ciudad y se corrobora que es igual al dato ingresado sale del bucle.
for i in meteorologia: 
    if i["ciudad"].lower() == consulta.lower(): 
        resultado_busqueda = i 
        break

#Aca una vez que tenemos un resultado para la búsqueda, lo mostramos por pantalla. 
if resultado_busqueda:     
    print(f"En la ciudad {resultado_busqueda['ciudad']}, hacen {resultado_busqueda['temperatura']} grados centígrados.")
else: 
    print("Error. No se encontró la ciudad que estás buscando")


