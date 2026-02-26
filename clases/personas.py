class Persona(object):
    def __init__(self):
        self.nombre=""
        self.apellidos="" 
        
    def leerDatosPersona(self): 
        self.nombre = input("Nombre:") 
        self.apellidos = input("Apellidos:")
        
    def mostrarDatosPersona(self): 
        print(self.nombre,self.apellidos) 
        