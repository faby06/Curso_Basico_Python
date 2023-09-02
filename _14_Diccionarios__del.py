#Diccionarios usando ciclo for 
print("Bienvenido a Gonvil\n")
libro1 = { #Con este simbolo { } se representan los diccionarios esto nos ayuda ya que puede funcionar como un catalogo 
    'Libro': 'Cien years de soledad',
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
del libro3 #Usando del se elimina todo el diccionario 
del libro1['Categoria'] #aqui se especifica que quiero borrar 
del libro1['Precio']
print('El autor es:',libro1['Autor'],'\nEl libro se llama:',libro1['Libro'])#borre anteiormente categoria y precio por eso solo me va imprimir el autor 
