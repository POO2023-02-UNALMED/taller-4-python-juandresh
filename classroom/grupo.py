from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self._listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista=[]
        lista.append(alumno)
        self._listadoAlumnos = self._listadoAlumnos + lista

    def __str__(self):
        asignatura_str = ', '.join(map(str, self._asignaturas))
        alumnos_str = ', '.join(self._listadoAlumnos)
        return f"{self._grupo}\n{asignatura_str}\n{self.grado}\n{alumnos_str}"

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 6"):
    #   cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 6"):
    #    cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 6"):
    #    cls.grado = nombre
