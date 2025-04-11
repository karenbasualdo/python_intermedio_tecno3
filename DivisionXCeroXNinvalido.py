#Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario
print("********INGRESE DOS NUMEROS PARA SU DIVISIÓN*******")

try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    try:
        div = numero1 / numero2
        print(f"La división entre {numero1} y {numero2} es: {div}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

except ValueError:
    print("Error: Uno de los valores ingresados no es un número válido.")

print("*******GRACIAS POR INGRESAR AL SISTEMA*******")