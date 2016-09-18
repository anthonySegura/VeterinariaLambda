dividir = lambda lista, n : [lista[i:i+n] for i in range(0, len(lista) , n)]
filtrarEliminados = lambda lista : list(filter(lambda x : x.STATUS["borrar"] == False, lista))
#Insercion de los objetos en las listas con polimorfismo
def insertarObjeto(objeto, lista, **atributos):
    objeto.crear(**atributos)
    objeto.STATUS["insertar"] = True
    lista.append(objeto)

#Llama este metodo al cargar las listas desde la BD
def cargarObjeto(objeto, lista, **atributos):
    objeto.crear(**atributos)
    lista.append(objeto)

#Modifica los objetos con polimorfismo
#!Tratar de hacerlo funcional
def modificarObjeto(objeto, listas , **nuevosAtributos):
    id = objeto.getID()
    objeto.STATUS["actualizar"][0] = True
    objeto.STATUS["actualizar"][2] = id
    if objeto.modificar(listas, **nuevosAtributos) == False:
        return False
    #Se buscan en todas las listas los objetos que tengan al objeto modificado como llave foranea
    for l in listas:
        for j in l:
           for x in list(j.getColumnsData().values()):
               if id in x:
                   #una vez encontrado el objeto se actualiza la llave foranea con el valor actual
                   j.modificar(listas,**{objeto.nombreTabla : objeto.getID()})

#Antes de modificar la llave de un objeto se verifica que esa llave no exista en la tabla para evitar errores en la base de datos.
#Retorna False en caso de existir ya la llave en la tabla. True si no hay problemas de llaves.
#!Tratar de hacer funcional
def verificarLlave(objeto, nuevoID ,listas):
    for lista in listas:
        for obj in lista:
            for valores in list(obj.getColumnsData().values()):
                if objeto.nombreTabla == obj.nombreTabla:
                    if nuevoID == obj.getID():
                        return False
    return True

#Antes de borrar un objeto verifica que no este relacionado con otros mediante las llaves foraneas
#!Tratar de hacer funcional
def verificarBorrado(objeto, listas):
    for l in listas:
        for j in l:
           for x in list(j.getColumnsData().values()):
               if objeto.getID() in x and objeto.getID() != j.getID():
                   return False
    return True


#Verifica si un objeto se encuentra en la lista
#Regresa True si el objeto esta en la lista
def verificarPorID(id, lista):
    return not list(filter(lambda x : x.getID() == id, lista)) == []

def buscarPorID(id, lista):
    if verificarPorID(id, lista):
        return lista[__buscarObjeto(id, lista)]

#Antes de llamar estas funciones se debe verificar que los objetos existan en la lista si no gg

#Elimina el objeto de la lista
__eliminarObjeto = lambda id, lista : lista.remove(list(filter(lambda x : x.getID() == id, lista))[0])
#Busca el objeto y lo marca para borrarlo luego en la base de datos
__marcarBorrado = lambda id, lista :  list(filter(lambda x : x.getID() == id, lista))[0].borrar()
#Regresa el indice del objeto en la lista
__buscarObjeto = lambda id, lista : lista.index(list(filter(lambda x : x.getID() == id, lista))[0])

#Regresa una lista con todas las dosis recomendadas para cierta enfermedad
dosisEnfermedad = lambda enfermedad, lista : list(filter(lambda x : x.enfermedad == enfermedad, lista))
#Regresa una lista con todas las dosis para cierto animal
dosisAnimal = lambda animal, lista : list(filter(lambda x : x.animal == animal, lista))

def borrarObjeto(id, lista):
    if verificarPorID(id, lista):
        __marcarBorrado(id, lista)