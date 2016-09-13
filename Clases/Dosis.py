
class Dosis:
    def __init__(self):
        self.id = ""
        self.animal = ""
        self.medicamento = ""
        self.enfermedad = ""
        self.rangoPeso = ""
        self.dosis = ""
        self.STATUS = {"borrar": False, "actualizar": False}

    def crear(self, **kwargs):
        self.id = kwargs["id"]
        self.animal = kwargs["animal"]
        self.medicamento = kwargs["medicamento"]
        self.enfermedad = kwargs["enfermedad"]
        self.rangoPeso = kwargs["rangoPeso"]
        self.dosis = kwargs["dosis"]

    def mofificar(self, **kwargs):
        self.id = kwargs["id"]
        self.animal = kwargs["animal"]
        self.medicamento = kwargs["medicamento"]
        self.enfermedad = kwargs["enfermedad"]
        self.rangoPeso = kwargs["rangoPeso"]
        self.dosis = kwargs["dosis"]

    def getID(self):
        return self.id

    def borrar(self):
        self.STATUS["borrar"] = True
