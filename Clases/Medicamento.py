from utilities.Funciones import verificarLlave

class Medicamento:
    def __init__(self):
        self.nombre = ""
        self.descripcion = ""
        self.foto = ""
        self.STATUS = {"borrar": False, "actualizar": [False, {}, "idAnterior"], "insertar": False}
        self.nombreTabla = ""

    def crear(self, **kwargs):
        self.nombre = kwargs["nombre"]
        self.descripcion = kwargs["descripcion"]
        self.foto = kwargs["foto"]
        self.nombreTabla = kwargs["nombreTabla"]

    def modificar(self,listas ,**kwargs):
        keys = kwargs.keys()
        ret = True
        if "nombre" in keys:
            if verificarLlave(self, kwargs["nombre"], listas):
                self.nombre = kwargs["nombre"]
            else:
                ret = False
        if "descripcion" in keys:
            self.descripcion = kwargs["descripcion"]
        if "foto" in keys:
            self.foto = kwargs["foto"]
        self.STATUS["actualizar"][1] = self.getColumnsData()
        return ret

    def getID(self):
        return self.nombre

    def getIDIdentifier(self):
        return "nombre"

    def getColumnsData(self):
        return {"nombre" : ["%s", self.nombre], "descripcion" : ["%s", self.descripcion], "foto" : ["%s", self.foto]}

    def borrar(self):
        self.STATUS["borrar"] = True
