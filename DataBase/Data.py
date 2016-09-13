from DataBase.conection import connection
from utilities.Funciones import *
from functools import reduce
from Clases.Usuario import Usuario
from Clases.Animal import Animal
from Clases.Dosis import Dosis
from Clases.Enfermedad import Enfermedad
from Clases.Medicamento import Medicamento
from Clases.Prescripcion import Prescripcion

'''
    Aca se guardan las listas con los datos de las tablas de la base de datos y otras funciones que
    tengan que ver con el manejo de la info de la BD
'''

USERS = []
ANIMALES = []
DOSIS = []
ENFERMEDADES = []
PRESCRIPCIONES = []
MEDICAMENTOS = []

TODO = [USERS, ANIMALES, DOSIS, ENFERMEDADES, PRESCRIPCIONES, MEDICAMENTOS]

def generador(lista):
    i = 0
    while i < len(lista):
        yield lista[i]
        i += 1

def cargarUsuarios():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `usuario`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Usuario()
            cargarObjeto(temp, USERS, username = x['username'], nombre = x['nombre'], passw = x['pass'],
                           foto = x['foto'], admin = x['admin'])
            x = cursor.fetchone()

def cargarAnimales():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `animal`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Animal()
            cargarObjeto(temp, ANIMALES, nombre=x['nombre'], descripcion=x['descripcion'], foto=x['foto'])
            x = cursor.fetchone()

def cargarDosis():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `dosis`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Dosis()
            cargarObjeto(temp, DOSIS, id = x['ID'], animal = x['animal'], medicamento = x['medicamento'],
                           enfermedad = x['enfermedad'], rangoPeso = x['rango-peso'], dosis = x['dosis'])
            x = cursor.fetchone()

def cargarEnfermedades():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `enfermedad`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Enfermedad()
            cargarObjeto(temp, ENFERMEDADES, nombre = x['nombre'], descripcion = x['descripcion'], foto = x['foto'])
            x = cursor.fetchone()

#Carga las listas con todos los datos de la base de datos.
def cargarDatos():
    cargarUsuarios()
    cargarAnimales()
    cargarDosis()
    cargarEnfermedades()

def insertarSQL(nombreTabla, **valores):
    '''
    :param nombreTabla: nombre exacto de la tabla en donde se va a insertar
    :param valores: claves-valor ; ejemplo username = [%s, "Rata Blanca"]. El valor es una lista
    la primera posicion es el tipo de dato la segunda el dato.
    :return:
    '''
    keys = [k for k in valores.keys()]
    with connection.cursor() as cursor:
        sql = "INSERT INTO " + nombreTabla + " (" + reduce(lambda x, y: x + "," + y, keys) \
              + ") " + "VALUES (" + reduce(lambda x, y: x + "," + y, [valores[i][0] for i in keys]) + ")"
        print(sql)
        tupla = tuple([valores[i][1] for i in valores])
        cursor.execute(sql, tupla)
        connection.commit()


#Corregir para cuando el numero de valores sea impar
def updateSQL(nombreTabla, where , **valores):
    '''
    :param nombreTabla: nombre exacto de la tabla
    :param valores: claves-valor ; ejemplo ["username", %s, "Rata Blanca"]. El valor es una lista, nombre de columna en comillas
    :param where: tupla ; ejemplo (username, %s , "Rata Blanca")
    :return:
    '''
    keys = [k for k in valores.keys()]
    concatenar = lambda x : reduce(lambda a , b : a + "," + b, list(map(lambda a : a + "=" + valores[a][0], x)))
    with connection.cursor() as cursor:
        sql = "UPDATE " + nombreTabla + " SET " + concatenar(keys) + " WHERE " + str(where[0]) + "=" + str(where[1])
        tupla = tuple([valores[i][1] for i in valores] + [where[2]])
        cursor.execute(sql, tupla)
        connection.commit()

def deleteSQL(nombreTable, where):
    '''
    :param nombreTable: nombre exacto de la tabla
    :param where: claves-valor ; ejemplo ["username" , %s, "Rata Blanca"]. El valor es una lista
    :return:
    '''
    with connection.cursor() as cursor:
        sql = "DELETE FROM " + nombreTable + " WHERE " + str(where[0]) + "=" + str(where[1])
        cursor.execute(sql, (where[2]))
        connection.commit()

def actualizarTablaBD(nombreTabla, lista):
    #Cada elemento de la lista se obtiene con el generador
    g = generador(lista)
    for i in range(len(lista)):
        objeto = g.__next__()
        where = (objeto.getIDIdentifier(), "%s", objeto.getID())
        if objeto.STATUS["borrar"]:
            deleteSQL(nombreTabla, where)

        elif objeto.STATUS["actualizar"][0]:
            whereUpdate = (objeto.getIDIdentifier(), "%s", objeto.STATUS["actualizar"][2])
            updateSQL(nombreTabla, whereUpdate, **objeto.getColumnsData())

        elif objeto.STATUS["insertar"]:
            insertarSQL(nombreTabla, **objeto.getColumnsData())


def actualizarBD():
    actualizarTablaBD("usuario", USERS)
    actualizarTablaBD("animal", ANIMALES)
    actualizarTablaBD("dosis", DOSIS)
    actualizarTablaBD("medicamentos", MEDICAMENTOS)
    actualizarTablaBD("prescripcion", PRESCRIPCIONES)
    actualizarTablaBD("enfermedad", ENFERMEDADES)

cargarDatos()
#modificarObjeto(ANIMALES[buscarObjeto("Taltuza", ANIMALES)],TODO, **{"descripcion" : "Tardigrado" } )
#insertarSQL("dosis", **{"id" : ["%s","4/20"], "animal" : ["%s","Caballo"], "medicamento" : ["%s", "Paracetamol"], "enfermedad" : ["%s","Tufillo"], "rango-peso" : ["%s", "10-20KG"],"dosis" : ["%s","20mg/8hrs"]})
#insertarObjeto(Dosis(), DOSIS, id = "4/20", animal = "Caballo", medicamento = "Paracetamol", enfermedad = "Tufillo", rangoPeso = "10-20KG", dosis = "20mg/8hrs" )

o = buscarPorID("Caballo",  ANIMALES)
modificarObjeto(o, TODO, nombre = "Taltuza")
for d in DOSIS:
    print(d.animal)
#actualizarBD()