from DataBase.conection import connection
import pymysql.err
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

LISTAS = [USERS, ANIMALES, DOSIS, ENFERMEDADES, PRESCRIPCIONES, MEDICAMENTOS]

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
                           foto = x['foto'], admin = x['admin'], nombreTabla = "usuario")
            x = cursor.fetchone()

def cargarAnimales():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `animal`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Animal()
            cargarObjeto(temp, ANIMALES, nombre=x['nombre'], descripcion=x['descripcion'], foto=x['foto'], nombreTabla = "animal")
            x = cursor.fetchone()

def cargarDosis():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `dosis`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Dosis()
            cargarObjeto(temp, DOSIS, id = x['ID'], animal = x['animal'], medicamento = x['medicamento'],
                           enfermedad = x['enfermedad'], rangoPeso = x['rangoPeso'], dosis = x['dosis'], nombreTabla = "dosis")
            x = cursor.fetchone()

def cargarEnfermedades():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `enfermedad`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Enfermedad()
            cargarObjeto(temp, ENFERMEDADES, nombre = x['nombre'], descripcion = x['descripcion'], foto = x['foto'], nombreTabla = "enfermedad")
            x = cursor.fetchone()

def cargarPrescripciones():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `prescripcion`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Prescripcion()
            cargarObjeto(temp, PRESCRIPCIONES, id = x['id'], usuario = x['usuario'], animal = x['animal'], enfermedad = x['enfermedad'], peso = x['peso'],
                         dosis = x['dosis'], nombreTabla = "prescripcion")
            x = cursor.fetchone()

def cargarMedicamentos():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `medicamentos`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Medicamento()
            cargarObjeto(temp, MEDICAMENTOS, nombre = x['nombre'], descripcion = x['descripcion'], foto = x['foto'], nombreTabla = "medicamentos")
            x = cursor.fetchone()

#Carga las listas con todos los datos de la base de datos.
def cargarDatos():
    cargarUsuarios()
    cargarAnimales()
    cargarDosis()
    cargarEnfermedades()
    cargarPrescripciones()
    cargarMedicamentos()

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
        try:
            cursor.execute(sql, tupla)
            connection.commit()
        except pymysql.err.ProgrammingError as error:
            codigo, msj = error.args
            print("Error en MySQL. Codigo de error -> ", codigo, " Mensaje ->", msj)
            return False


def updateSQL(nombreTabla, where , **valores):
    '''
    :param nombreTabla: nombre exacto de la tabla
    :param valores: claves-valor ; ejemplo ["username", %s, "Rata Blanca"]. El valor es una lista, nombre de columna en comillas
    :param where: tupla ; ejemplo (username, %s , "Rata Blanca")
    :return: False en caso de error
    '''
    keys = [k for k in valores.keys()]
    concatenar = lambda x : reduce(lambda a , b : a + "," + b, list(map(lambda a : a + "=" + valores[a][0], x)))
    with connection.cursor() as cursor:
        sql = "UPDATE " + nombreTabla + " SET " + concatenar(keys) + " WHERE " + str(where[0]) + "=" + str(where[1])
        tupla = tuple([valores[i][1] for i in valores] + [where[2]])
        try:
            cursor.execute(sql, tupla)
            connection.commit()
        except pymysql.err.ProgrammingError as error:
            codigo, msj = error.args
            print("Error en MySQL. Codigo de error -> ", codigo, " Mensaje ->", msj)
            return False

def deleteSQL(nombreTable, where):
    '''
    :param nombreTable: nombre exacto de la tabla
    :param where: claves-valor ; ejemplo ["username" , %s, "Rata Blanca"]. El valor es una lista
    :return:
    '''
    with connection.cursor() as cursor:
        sql = "DELETE FROM " + nombreTable + " WHERE " + str(where[0]) + "=" + str(where[1])
        try:
            cursor.execute(sql, (where[2]))
            connection.commit()
        except pymysql.err.ProgrammingError as error:
            codigo, msj = error.args
            print("Error en MySQL. Codigo de error -> ", codigo, " Mensaje ->", msj)
            return False

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

