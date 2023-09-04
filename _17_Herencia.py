# Clases y objetos
class Persona(): #Usando class es como se crea una clase 
    # El método __init__ se llama automáticamente cuando se crea un objeto de la clase.
    def __init__(self, nombre, edad,apellido):
        # self se utiliza para hacer referencia a cualquier objeto que queramos.
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        

    def Imprimir(self):
        print('Nombre:', self.nombre,'\nApellido:',self.apellido, '\nEdad:', self.edad)

# Creamos una instancia de la clase Persona
persona1 = Persona('Faby',23,'Castro')
#Llamamos al metodo imprimir de la instancia persona1
persona1.Imprimir() #Esto imprimir mi nombre,apellido y mi edad.

#Herencia 
class Materia(Persona):
    def __init__(self, nombre, edad,apellido, materia):
        # Llamamos al constructor de la clase padre usando super()
        super().__init__(nombre, edad,apellido)
        # Agregamos una variable de instancia adicional
        self.materia = materia
        
    def Imprimir2(self):
        print('Nombre:', self.nombre,'\nApellido:',self.apellido, '\nEdad:', self.edad,'\nMateria:',self.materia)
        
#Creamos una instancia de la subclase Estudiante
materia1= Materia('Pablo', 20,'Lopez','Quimica')
materia1.Imprimir2()
