#Escribe un programa que intente acceder a una clave que no existe
#en un diccionario. Si se produce una excepción KeyError, captura la
#excepción y muestra
print("******** El Juego de los Colores SECRETO*******")
print
dicc= {"cielo":"celeste","sol":"amarallo","mar":"azul","pasto":"verde"}

try:
    clave = input("Ingrese un objecto para buscar en el diccionario: ")
    valor = dicc[clave]
    print(f"El valor asociado a la clave '{clave}' es: {valor}")

except KeyError:
    print(f"Error: La clave '{clave}' no existe en el diccionario.")

print("*******GRACIAS POR INGRESAR AL SISTEMA*********")