
class Prescripcion:
    def __init__(self):
        self.id = ""
        self.usuario = ""
        self.animal = ""
        self.enfermedad = ""
        self.peso = 0
        self.dosis = ""
        self.STATUS = {"borrar": False, "actualizar": False}

    def crear(self, **kwargs):
        self.id = kwargs["id"]
        self.usuario = kwargs["usuario"]
        self.animal = kwargs["animal"]
        self.enfermedad = kwargs["enfermedad"]
        self.peso = kwargs["peso"]
        self.dosis = kwargs["dosis"]

    def modificar(self, **kwargs):
        self.id = kwargs["id"]
        self.usuario = kwargs["usuario"]
        self.animal = kwargs["animal"]
        self.enfermedad = kwargs["enfermedad"]
        self.peso = kwargs["peso"]
        self.dosis = kwargs["dosis"]

    def getID(self):
        return self.id

    def borrar(self):
        self.STATUS["borrar"] = True