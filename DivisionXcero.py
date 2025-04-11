#Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario
print("********INGRESE DOS NUMEROS PARA SU DIVISIÓN*******")
numero1=float(input ("ingrese un número: "))
numero2= float(input("ingrese el segundo numero"))

try:
    div= numero1/numero2
    print (f"la división entre ambos número es {div}")
except ZeroDivisionError:
    print("no se puede dividir por 0")
    
print("*******GRACIAS POR INGRESAR AL SISTEMA*********")