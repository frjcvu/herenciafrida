class Persona(object): 
 
  def __init__(self): 
    self.nombre="" 
    self.apellidos="" 
 
  def leerDatosPersona(self): 
    self.nombre = input("Nombre:") 
    self.apellidos = input("Apellidos:") 
 
  def mostrarDatosPersona(self): 
    print(self.nombre,self.apellidos) 
   
class Alumno(Persona): 
 
  def __init__(self): 
    self.cuenta="" 
   
  def leerDatosAlumno(self): 
    self.cuenta = input("Cuenta:") 
 
  def mostrarDatosAlumno(self): 
    print(self.cuenta)   
 
class Profesor(Persona): 
  def __init__(self): 
    super().__init__()#Llamada al init de la super clase 
    self.clave = "" 
   
  def leerDatosProfesor(self): 
    self.clave = input("Clave profesor: ") 
 
  def mostrarDatosProfesor(self):
      print(self.clave) 
      
class Exalumno(Alumno,Profesor): 
    def __init__(self): 
        super().__init__() 
        self.titulo = "" 
    def leerDatosExalumno(self): 
        self.titulo = input("Título del exalumno: ") 
    def mostrarDatosExalumno(self): 
        print(self.titulo) 