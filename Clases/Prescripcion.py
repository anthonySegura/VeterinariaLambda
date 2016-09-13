
class Prescripcion:
    def __init__(self):
        self.id = ""
        self.usuario = ""
        self.animal = ""
        self.enfermedad = ""
        self.peso = 0
        self.dosis = ""
        self.STATUS = {"borrar": False, "actualizar": [False, {}, "idAnterior"], "insertar": False}

    def crear(self, **kwargs):
        self.id = kwargs["id"]
        self.usuario = kwargs["usuario"]
        self.animal = kwargs["animal"]
        self.enfermedad = kwargs["enfermedad"]
        self.peso = kwargs["peso"]
        self.dosis = kwargs["dosis"]

    def modificar(self, **kwargs):
        keys = kwargs.keys()
        if "id" in keys:
            self.id = kwargs["id"]
        if "usuario" in keys:
            self.usuario = kwargs["usuario"]
        if "animal" in keys:
            self.animal = kwargs["animal"]
        if "enfermedad" in keys:
            self.enfermedad = kwargs["enfermedad"]
        if "peso" in keys:
            self.peso = kwargs["peso"]
        if "dosis" in keys:
            self.dosis = kwargs["dosis"]
        self.STATUS["actualizar"][1] = self.getColumnsData()

    def getID(self):
        return self.id

    def getIDIdentifier(self):
        return "id"

    def getColumnsData(self):
        return {"id" : ["%s", self.id], "usuario" : ["%s", self.usuario], "animal" : ["%s", self.animal],
                "enfermedad" : ["%s", self.enfermedad], "peso" : ["%s", self.peso], "dosis" : ["%s", self.dosis]}

    def borrar(self):
        self.STATUS["borrar"] = True