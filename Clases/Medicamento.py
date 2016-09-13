
class Medicamento:
    def __init__(self):
        self.nombre = ""
        self.descripcion = ""
        self.foto = ""
        self.STATUS = {"borrar": False, "actualizar": False}

    def crear(self, **kwargs):
        self.nombre = kwargs["nombre"]
        self.descripcion = kwargs["descripcion"]
        self.foto = kwargs["foto"]

    def modificar(self, **kwargs):
        self.nombre = kwargs["nombre"]
        self.descripcion = kwargs["descripcion"]
        self.foto = kwargs["foto"]

    def getID(self):
        return self.nombre

    def borrar(self):
        self.STATUS["borrar"] = True
