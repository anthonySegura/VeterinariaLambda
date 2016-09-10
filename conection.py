import pymysql

from Clases.Usuario import *
from Clases.Animal import *
import Clases.Usuario
from utilities.Funciones import *
from functools import reduce

connection = pymysql.connect(host='localhost',
                             user='anthony',
                             password='1234567',
                             db='veterinaria',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

"""with connection.cursor() as cursor:
    sql = "INSERT INTO `usuario` (`username`, `pass`,`nombre`,`admin`,`foto`) VALUES (%s, %s,%s,%s,%s)"
    cursor.execute(sql, ('josdead', '1234','Jose Miguel Murillo R','1','a.jpg'))
    connection.commit()"""

users = []
animales = []

'''
def insertarSQL(tabla, *values):
    with connection.cursor() as cursor:
        sql = "INSERT INTO " + tabla + " VALUES (" + reduce( lambda a , b :  a + "," +  b , list(map(lambda x : str(x), values ))) + ")"
        cursor.execute(sql)
        connection.commit()
'''

def obtenerUsuarios():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `usuario`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Usuario()
            insertarObjeto(temp, users, username = x['username'], nombre = x['nombre'], passw = x['pass'],
                           foto = x['foto'], admin = x['admin'])
            x = cursor.fetchone()

def obtenerAnimales():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `animal`"
        cursor.execute(sql)
        x = cursor.fetchone()
        while (x != None):
            temp = Animal()
            insertarObjeto(temp, animales, nombre=x['nombre'], descripcion=x['descripcion'], foto=x['foto'])
            x = cursor.fetchone()

obtenerAnimales()
print(len(animales))
marcarBorrado("Caballo", animales)
print(animales[0].STATUS)


