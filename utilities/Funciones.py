

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
def modificarObjeto(objeto, **nuevosAtributos):
    objeto.modificar(**nuevosAtributos)
    objeto.STATUS["actualizar"][0] = True

#Verifica si un objeto se encuentra en la lista
#Regresa True si el objeto esta en la lista
def buscarPorID(id, lista):
    return not list(filter(lambda x : x.getID() == id, lista)) == []

#Antes de llamar estas funciones se debe verificar que los objetos existan en la lista si no gg

#Elimina el objeto de la lista
__eliminarObjeto = lambda id, lista : lista.remove(list(filter(lambda x : x.getID() == id, lista))[0])
#Busca el objeto y lo marca para borrarlo luego en la base de datos
__marcarBorrado = lambda id, lista :  list(filter(lambda x : x.getID() == id, lista))[0].borrar()
#Regresa el indice del objeto en la lista
buscarObjeto = lambda id, lista : lista.index(list(filter(lambda x : x.getID() == id, lista))[0])

#Regresa una lista con todas las dosis recomendadas para cierta enfermedad
dosisEnfermedad = lambda enfermedad, lista : list(filter(lambda x : x.enfermedad == enfermedad, lista))
#Regresa una lista con todas las dosis para cierto animal
dosisAnimal = lambda animal, lista : list(filter(lambda x : x.animal == animal, lista))

def borrarObjeto(id, lista):
    if buscarPorID(id, lista):
        __marcarBorrado(id, lista)