#Bucle while
contador = 0

while contador <= 5: #Se ejecutara mientras la variable contador sea menor que 5,El bucle se detendrá cuando contador llegue a 5, ya que la condición contador <= 5 se volverá falsa.
    print("El contador es:", contador)
    contador += 1#Cada vez que se ejecuta el bucle, se imprime el valor de contador y se incrementa en 1

#Uso de break 
contador2 = 1
while contador2 <=10:
    print("El segundo contador es:",contador2)
    if contador2==4:
        break #Aqui se rompe el ciclo y por esa razon solo llega hasta 4 y no al 10 
    contador2+=1

#Uso de continue
contador3 = 0
while contador3<=10:
    contador3+=1
    if contador3 == 5 or contador3 == 7:
       continue #Esto lo que hace es saltarse el 5 y el 7  
    print("El tercer contador es:",contador3)
 