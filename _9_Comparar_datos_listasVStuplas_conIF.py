#Comparar Datos en listas y tublas con IF
materia=input("Introduce una materia:\n")
nombre=['Matematicas','Historia','Electronica','Dinamica','PLCS']
if materia in nombre: #Aqui dice que si materia esta dentro de la lista nombre haga el print si no con el else va mandar otro print
    print("Tienes esta materia este semestre")
else:
    print("Esta materia no la tienes este semestre")
    
