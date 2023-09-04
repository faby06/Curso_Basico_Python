#Manejo de excepciones 
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No puedes dividir entre cero.")
    except TypeError:
        print("Error: Asegurate de que ambos valores sean numeros.")
    except Exception as e: # Captura cualquier excepcion no manejada anteriormente y muestra un mensaje de error
        print(f"Se produjo un error: {e}")
    else:# Se ejecuta si no se ha producido ninguna excepcion y muestra el resultado de la división
        print(f"El resultado de la division es: {resultado}")
    finally:
        print("Este bloque siempre se ejecutara, se haya producido una excepcion o no.")
# Se crea un bucle infinito para permitir al usuario realizar multiples divisiones
while True:
    try:
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        dividir(a, b)
    except ValueError:
        print("Error: Debes ingresar numeros validos.")
    respuesta = input("Deseas realizar otra division (S/N):")
    if respuesta.upper() != 'S':
        break