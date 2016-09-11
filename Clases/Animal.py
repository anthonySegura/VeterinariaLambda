
class Animal:
    def __init__(self):
        self.nombre = ""
        self.descripcion = ""
        self.foto = ""
        self.STATUS = {"borrar": False, "actualizar": [False, {}], "insertar" : False}

    def crear(self, **kwargs):
        self.nombre = kwargs["nombre"]
        self.descripcion = kwargs["descripcion"]
        self.foto = kwargs["foto"]

    def modificar(self, **kwargs):
        keys = kwargs.keys()
        if "nombre" in keys:
            self.nombre = kwargs["nombre"]
        if "descripcion" in keys:
            self.descripcion = kwargs["descripcion"]
        if "foto" in keys:
            self.foto = kwargs["foto"]
        self.STATUS["actualizar"][1] = self.getColumnsData()

    def getID(self):
        return self.nombre

    def getIDIdentifier(self):
        return "nombre"

    def getColumnsData(self):
        return {"nombre" : ["%s", self.nombre], "descripcion" : ["%s", self.descripcion], "foto" : ["%s", self.foto]}

    def borrar(self):
        self.STATUS["borrar"] = True