from utilities.Funciones import verificarLlave

class Usuario():
    def __init__(self):
        self.username = ""
        self.nombre = ""
        self.passw = ""
        self.foto = ""
        self.admin = 0
        #Marca que indica si se debe borrar o actualizar el registro original en la base de datos.
        self.STATUS = {"borrar": False, "actualizar": [False, {}, "idAnterior"], "insertar": False}
        self.nombreTabla = ""

    def crear(self, **kwargs):
        self.username = kwargs["username"]
        self.nombre = kwargs["nombre"]
        self.passw = kwargs["passw"]
        self.foto = kwargs["foto"]
        self.admin = kwargs["admin"]
        self.nombreTabla = kwargs["nombreTabla"]

    def modificar(self,listas ,**kwargs):
        keys = kwargs.keys()
        ret = True
        if "username" in keys:
            if verificarLlave(self, kwargs["username"], listas):
                self.username = kwargs["username"]
            else:
                ret = False
        if "nombre" in keys:
            self.nombre = kwargs["nombre"]
        if "passw" in keys:
            self.passw = kwargs["passw"]
        if "foto" in keys:
            self.foto = kwargs["foto"]
        if "admin" in keys:
            self.admin = kwargs["admin"]
        self.STATUS["actualizar"][1] = self.getColumnsData()
        return ret

    def getID(self):
        return self.username

    def getIDIdentifier(self):
        return "username"

    def getColumnsData(self):
        return {"username" : ["%s", self.username], "nombre" : ["%s", self.nombre], "pass" : ["%s", self.passw],
                "foto" : ["%s", self.foto], "admin" : ["%s", self.admin]}

    def borrar(self):
        self.STATUS["borrar"] = True
