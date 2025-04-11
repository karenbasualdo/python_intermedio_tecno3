#Escribe un programa que intente sumar un número y una cadena. Si se produce
#un error de tipo, captura la excepción TypeError y muestra un mensaje de
#error al usuario. 
print("********INGRESE un NUMEROS y una PALABRA*******")
numero1=int(input ("ingrese un número: "))
cadena= str(input("ingrese una palabra"))

try:
    sumar = numero1 + cadena
    print (f"la división entre ambos número es {sumar}")
except TypeError:
    print("no se puede sumar un numero y una palabra")
    
print("*******GRACIAS POR INGRESAR AL SISTEMA*********")