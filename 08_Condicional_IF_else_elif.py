#Condicional IF
num1 = 60   #Se declaran 2 varibles y se les asigna un valor 
num2 = 50

if num1<=num2: # Esta comparando estas dos varibles dice que si num1 es menor o igual que num2 se imprima el string 
 print ("Si es verdadero")
# ELSE
else:
 print("Es falso") #Si el if no se cumple va ejecutar el else con el siguiente string 
 
#IF,ELSE,ELIF

print("\nBienvenido al Store Ba")
a=int(input("Introduce tu edad:\n")) #el input se utliza para que el usuario ingrese su respuesta 

if a <=0:
 print("No puedes tener esa edad")
elif a>=1 and a<=17:
 print("Eres menor de edad no puedes ingresar ") #los elif son para agregar mas condiciones las que tu quieras
elif a>=18 and a<=99:
 print("Pues iniciar tus compras")
else:
 print("Edad no valida")
 
