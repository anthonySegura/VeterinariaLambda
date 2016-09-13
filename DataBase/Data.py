from DataBase.conection import connection
from utilities.Funciones import *
from functools import reduce
from Clases.Usuario import *
from Clases.Animal import *
from Clases.Dosis import *
from Clases.Enfermedad import *
from Clases.Medicamento import *
from Clases.Prescripcion import *

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

def cargarUsuarios():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `usuario`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Usuario()
            insertarObjeto(temp, USERS, username = x['username'], nombre = x['nombre'], passw = x['pass'],
                           foto = x['foto'], admin = x['admin'])
            x = cursor.fetchone()

def cargarAnimales():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `animal`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Animal()
            insertarObjeto(temp, ANIMALES, nombre=x['nombre'], descripcion=x['descripcion'], foto=x['foto'])
            x = cursor.fetchone()

def cargarMedicamentos():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `medicamentos`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Medicamento()
            insertarObjeto(temp, MEDICAMENTOS, nombre=x['nombre'], descripcion=x['descripcion'], foto=x['foto'])
            x = cursor.fetchone()

def cargarPrescripciones():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `prescripcion`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Prescripcion()
            insertarObjeto(temp, PRESCRIPCIONES, id = x['id'], usuario = x['usuario'], animal = x['animal'],
                           enfermedad = x['enfermedad'], peso = x['peso'], dosis = x['dosis'])
            x = cursor.fetchone()

def cargarDosis():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `dosis`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Dosis()
            insertarObjeto(temp, DOSIS, id = x['ID'], animal = x['animal'], medicamento = x['medicamento'],
                           enfermedad = x['enfermedad'], rangoPeso = x['rangoPeso'], dosis = x['dosis'])
            x = cursor.fetchone()



#Carga las listas con todos los datos de la base de datos.
def cargarDatos():
    cargarUsuarios()
    cargarAnimales()
    cargarDosis()
    cargarMedicamentos()
    cargarPrescripciones()



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
        tupla = tuple([valores[i][1] for i in valores])
        cursor.execute(sql, tupla)
        connection.commit()

def updateSQL(nombreTabla, where , **valores):
    '''
    :param nombreTabla: nombre exacto de la tabla
    :param valores: claves-valor ; ejemplo ["username", %s, "Rata Blanca"]. El valor es una lista, nombre de columna en comillas
    :param where: tupla ; ejemplo (username, %s , "Rata Blanca")
    :return:
    '''
    keys = [k for k in valores.keys()]
    with connection.cursor() as cursor:
        sql = "UPDATE " + nombreTabla + " SET " + reduce( lambda a , b : a + "=" + valores[a][0]
               + ", " + b + "=" + valores[b][0], keys) + " WHERE " + str(where[0]) + "=" + str(where[1])
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

#ID,animal,medicamentos,enfermedad,rango-peso,dosis

#insertarSQL("dosis", **{"id" : ["%s", "4/20"], "animal" : ["%s", "Caballo"], "medicamento" : ["%s", "AINIL"], "enfermedad" : ["%s", "BRUCELÓSIS"], "rangoPeso" : ["%s", "100/50kg"],"dosis": ["%s","Dos al dia"]})
#insertarSQL("dosis", **{"id" : ["%s", "4/21"], "animal" : ["%s", "Perro"], "medicamento" : ["%s", "ANESMOL"], "enfermedad" : ["%s", "BRUCELÓSIS"], "rangoPeso" : ["%s", "20/10kg"],"dosis": ["%s","Dos al dia"]})
#insertarSQL("dosis", **{"id" : ["%s", "4/22"], "animal" : ["%s", "Vaca"], "medicamento" : ["%s", "BAYTRIL"], "enfermedad" : ["%s", "BRUCELÓSIS"], "rangoPeso" : ["%s", "300/100kg"],"dosis": ["%s","Dos al dia"]})
#insertarSQL("dosis", **{"id" : ["%s", "4/23"], "animal" : ["%s", "Llama"], "medicamento" : ["%s", "ACTIFUCIN"], "enfermedad" : ["%s", "BRUCELÓSIS"], "rangoPeso" : ["%s", "200/50kg"],"dosis": ["%s","Dos al dia"]})
#insertarSQL("dosis", **{"id" : ["%s", "4/24"], "animal" : ["%s", "Caballo5"], "medicamento" : ["%s", "DERFEN"], "enfermedad" : ["%s", "BRUCELÓSIS"], "rangoPeso" : ["%s", "200/100kg"],"dosis": ["%s","Dos al dia"]})

#updateSQL("enfermedad" , ("nombre", "%s", "Cancer") , nombre=["%s", "Rabia"], descripcion = ["%s" , "Rba"])
#deleteSQL("enfermedad", ("nombre","%s" ,"Rabia"))