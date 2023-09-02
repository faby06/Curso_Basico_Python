#Diccionarios usando ciclo for 
print("Bienvenido a Gonvil\n")
libro1 = { #Con este simbolo { } se representan los diccionarios esto nos ayuda ya que puede funcionar como un catalogo 
    'Libro': 'Cien de soledad',
    'Categoria': 'Novela',
    'Precio': '419.80',
    'Autor': 'Gabriel Garcia Marquez',
}
libro2 = {
    'Libro': 'El Hobbit',
    'Categoria': 'Fantasia',
    'Precio': '319.00',
    'Autor': 'J.R.R. Tolkien',
}
libro3 = {
    'Libro': 'Crimen y castigo',
    'Categoria': 'Novela clasica',
    'Precio': '250.00',
    'Autor': 'Fyodor Dostoevsky',
}
libro4 = {
    'Libro': 'Breve historia del tiempo',
    'Categoria': 'Ciencia',
    'Precio': '379.80',
    'Autor': 'Stephen Hawking',
}
for x in libro4:
	print(x, '=', libro4[x] + '.') #Estos nos sirve para mandar imprimir todo lo que tien el diccionario en este caso todo lo que tien libro 4