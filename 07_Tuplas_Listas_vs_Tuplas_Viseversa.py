#Crear y manejar Tuplas 
Cal=(70,90,80,"La suma de los parciales es:") #este signo de () representa las tuplas que son iguales a las listas solo que estas no las podemos modificar
print(Cal[3],round((Cal[0]+Cal[1]+Cal[2])/3,2))

#Convertir tuplas a listas
nombres=('Fabiola','Daniel','Erika','Pablo')
lista=list(nombres)
print(lista) #Las listas se diferencian con los ()

#Convierte listas a tuplas
nombres1=['Fabiola','Daniel','Erika','Pablo']
tupla=tuple(nombres1)
print(tupla) 
