
class Dosis:
    def __init__(self):
        self.id = ""
        self.animal = ""
        self.medicamento = ""
        self.enfermedad = ""
        self.rangoPeso = ""
        self.dosis = ""
        self.STATUS = {"borrar": False, "actualizar": [False, {}, "idAnterior"], "insertar": False}

    def crear(self, **kwargs):
        self.id = kwargs["id"]
        self.animal = kwargs["animal"]
        self.medicamento = kwargs["medicamento"]
        self.enfermedad = kwargs["enfermedad"]
        self.rangoPeso = kwargs["rangoPeso"]
        self.dosis = kwargs["dosis"]

    def modificar(self, **kwargs):
        keys = kwargs.keys()
        if "id" in keys:
            self.id = kwargs["id"]
        if "animal" in keys:
            self.animal = kwargs["animal"]
        if "medicamento" in keys:
            self.medicamento = kwargs["medicamento"]
        if "enfermedad" in keys:
            self.enfermedad = kwargs["enfermedad"]
        if "rangoPeso" in keys:
            self.rangoPeso = kwargs["rangoPeso"]
        if "dosis" in keys:
            self.dosis = kwargs["dosis"]
        self.STATUS["actualizar"][1] = self.getColumnsData()

    def getID(self):
        return self.id

    def getIDIdentifier(self):
        return "id"

    def getColumnsData(self):
        return {"id" : ["%s", self.id], "animal" : ["%s", self.animal], "medicamento" : ["%s", self.medicamento],
                "enfermedad" : ["%s", self.enfermedad], "rango-peso" : ["%s", self.rangoPeso], "dosis" : ["%s", self.dosis]}

    def borrar(self):
        self.STATUS["borrar"] = True
