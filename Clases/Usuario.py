class Usuario():
    def __init__(self):
        self.username = ""
        self.nombre = ""
        self.passw = ""
        self.foto = ""
        self.admin = 0
        self.STATUS = {"borrar": False, "actualizar": False}

    def crear(self, **kwargs):
        self.username = kwargs["username"]
        self.nombre = kwargs["nombre"]
        self.passw = kwargs["passw"]
        self.foto = kwargs["foto"]
        self.admin = kwargs["admin"]

    def modificar(self, **kwargs):
        self.username = kwargs["username"]
        self.nombre = kwargs["nombre"]
        self.passw = kwargs["passw"]
        self.foto = kwargs["foto"]
        self.admin = kwargs["admin"]

    def getID(self):
        return self.username

    def borrar(self):
        self.STATUS["borrar"] = True
