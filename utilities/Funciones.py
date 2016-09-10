
#Insercion de los objetos en las listas con polimorfismo
def insertarObjeto(objeto, lista, **atributos):
    objeto.crear(**atributos)
    lista.append(objeto)

#Modifica los objetos con polimorfismo
def modificarObjeto(objeto, **nuevosAtributos):
    objeto.modificar(**nuevosAtributos)

#Elimina el objeto de la lista
eliminarObjeto = lambda id, lista : lista.remove(list(filter(lambda x : x.getID() == id, lista))[0])
marcarBorrado = lambda id, lista :  list(filter(lambda x : x.getID() == id, lista))[0].borrar()

