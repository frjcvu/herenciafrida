from clases.alumnos import Alumno
from clases.profesores import Profesor
from clases.exalumnos import Exalumno

def main():
    #crear objeto de la clase
    #al=Alumno()
    #llamada a los metodos
    #al.leerDatosPersona()
    #al.leerDatosAlumno()
    #al.mostrarDatosPersona()
    #al.mostrarDatosAlumno()
    
    #prof=Profesor()
    #prof.leerDatosProfesor() 
    #prof.mostrarDatosProfesor() 

    #aplicacion de herencia multiple
    #crear objeto de la clase exalumno
    exa=Exalumno()
    exa.leerDatosPersona() 
    exa.leerDatosAlumno() 
    exa.leerDatosProfesor() 
    exa.leerDatosExalumno()
    print("********************") 
    exa.mostrarDatosPersona() 
    exa.mostrarDatosAlumno() 
    exa.mostrarDatosProfesor() 
    exa.mostrarDatosExalumno()
        
if __name__=="__main__":
    main()
    
