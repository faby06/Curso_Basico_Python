#funciones 
def multi(multi1, multi2): #Usando def es como se crean las funciones 
    result = multi1 * multi2
    return result
# Llama a la función multi con diferentes números de argumentos
result1 = multi(5, 6)
result2 = multi(10, 8)
result3 = multi(60, 90)

print("Resultado 1:", result1)
print("Resultado 2:", result2)
print("Resultado 3:", result3)

def suma(*args):
    result = 0  # Inicializamos el resultado en 1
    for num in args:
        result += num
    return result

# Llama a la función multi con diferentes números de argumentos
resultado1 = suma(9, 6)
resultado2 = suma(25,5)
resultado3 = suma(100,50)

print("Resultado 1:", resultado1)
print("Resultado 2:", resultado2)
print("Resultado 3:", resultado3)