from clases.personas import Persona
class Profesor(Persona): 
  def __init__(self): 
    super().__init__()#Llamada al init de la super clase 
    self.clave = "" 
   
  def leerDatosProfesor(self): 
    self.clave = input("Clave profesor: ") 
 
  def mostrarDatosProfesor(self):
       print(self.clave) 
       