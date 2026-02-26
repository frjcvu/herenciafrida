from clases.personas import Persona
class Alumno(Persona): 
    def __init__(self): 
        self.cuenta="" 
   
    def leerDatosAlumno(self): 
        self.cuenta = input("Cuenta:") 
 
    def mostrarDatosAlumno(self): 
        print(self.cuenta)   
        