from app import app
from flask import render_template,request,redirect,url_for
from DataBase.Data import *
from flask_paginate import Pagination
from utilities.Funciones import *

sesion=None

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    global sesion
    error=None
    if  request.method == 'POST':
        user = list(filter(lambda x: x.username ==str(request.form['username']) and x.passw == str(request.form['password']), USERS))
        if len(user)==0:
            error='Usuario o contraseña invalidos'
        else:
            sesion = user[0]
            return redirect(url_for('animals'))
    return render_template('login.html',error=error)



@app.route('/marico',methods=['GET','POST'])
def marico():
    lol="Overwatch"
    if request.method == 'POST':
        lol=request.form['text']
    return  render_template('menu.html', lol=lol)



@app.route('/animals',methods=['GET','POST'])
def animals():

    page = request.args.get('page', type=int, default=1)
    filtro=filtrarEliminados(ANIMALES)
    a=dividir(filtro,5)
    if(len(a)>0):
        animals =a[page-1]
    else: animals=[]

    pagination = Pagination(page=page,per_page=5,total=len(filtro), record_name='Animals')
    if request.method == 'POST':
        if request.form['text']=="":
            return redirect(url_for('animals'))
        animals=[buscarPorID(request.form['text'],filtro)]
        pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='Animals')
    global sesion
    user=sesion

    return render_template('animals.html',
                           animals=animals,
                           pagination=pagination,user=user,
                           )
@app.route('/animals/<text>',methods=['GET','POST'])
def animals1(text):
    page = request.args.get('page', type=int, default=1)
    global sesion
    filtro = filtrarEliminados(ANIMALES)
    animals = [buscarPorID(text, filtrarEliminados(filtro))]
    pagination = Pagination(page=page, per_page=5, total=len(animals), record_name='Animals')
    return render_template('animals.html',
                           animals=animals,
                           pagination=pagination,text=text,user=sesion)

@app.route('/enfermedad',methods=['GET','POST'])
def enfermedad():
    page = request.args.get('page', type=int, default=1)
    filtro=filtrarEliminados(ENFERMEDADES)
    a=dividir(filtro,5)
    if(len(a)>0):
        enfermedad =a[page-1]
    else: enfermedad=[]

    pagination = Pagination(page=page,per_page=5,total=len(filtro), record_name='Enfermedad')
    if request.method == 'POST':
        if request.form['text']=="":
            return redirect(url_for('animals'))
        enfermedad=[buscarPorID(request.form['text'],filtro)]
        pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='Enfermedad')
    global sesion
    user=sesion

    return render_template('enfermedad.html',
                           enfermedad=enfermedad,
                           pagination=pagination,user=user,
                           )
@app.route('/enfermedad/<text>',methods=['GET','POST'])
def enfermedad1(text):
    page = request.args.get('page', type=int, default=1)
    global sesion
    filtro = filtrarEliminados(ENFERMEDADES)
    enfermedad = [buscarPorID(text, filtrarEliminados(filtro))]
    pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='enfermedad')
    return render_template('enfermedad.html',
                           enfermedad=enfermedad,
                           pagination=pagination,text=text,user=sesion)
@app.route('/eliminar/<lista>/<text>', methods=['GET', 'POST'])
def eliminar(lista,text):
    lol=text
    if lista=="ANIMALES":
        objeto = buscarPorID(text, ANIMALES)
        if verificarBorrado(objeto, LISTAS):
            borrarObjeto(text,ANIMALES)
        return redirect(url_for('animals'))
    if lista=="DOSIS":
        objeto = buscarPorID(text,DOSIS)
        if verificarBorrado(objeto, LISTAS):
            borrarObjeto(text,DOSIS)
        return redirect(url_for('dosis_Enfermedad'))
    if lista=="MEDICAMENTOS":
        objeto = buscarPorID(text,MEDICAMENTOS)
        if verificarBorrado(objeto, LISTAS):
            borrarObjeto(text,MEDICAMENTOS)
        return redirect(url_for('medicamentos'))
    if lista=="ENFERMEDADES":
        objeto = buscarPorID(text,ENFERMEDADES)
        if verificarBorrado(objeto, LISTAS):
            borrarObjeto(text,ENFERMEDADES)
        return redirect(url_for('enfermedad'))
    if lista == "USERS":
        objeto = buscarPorID(text, USERS)
        global sesion
        if objeto==sesion:
            return redirect(url_for('usuarios'))
        else:
            if verificarBorrado(objeto, LISTAS):
                borrarObjeto(text, USERS)
            return redirect(url_for('usuarios'))

    else:
        objeto = buscarPorID(text, PRESCRIPCIONES)
        if verificarBorrado(objeto, LISTAS):
            borrarObjeto(text, PRESCRIPCIONES)
        return redirect(url_for('prescripcion'))

@app.route('/modificar/<lista>/<text>', methods=['GET', 'POST'])
def modificar(lista,text):
    lol=text
    global sesion
    error=None
    if lista == "ANIMALES":
        objeto = buscarPorID(text, ANIMALES)
        if request.method == 'POST':
            nombre=request.form['nombre']
            descripcion=request.form['descripcion']
            foto=request.form['foto']
            modificarObjeto(objeto,LISTAS,nombre=nombre,descripcion=descripcion,foto=foto)
            return redirect(url_for('animals'))
    if lista == "MEDICAMENTOS":
        objeto = buscarPorID(text, MEDICAMENTOS)
        if request.method == 'POST':
            nombre=request.form['nombre']
            descripcion=request.form['descripcion']
            foto=request.form['foto']
            modificarObjeto(objeto,LISTAS,nombre=nombre,descripcion=descripcion,foto=foto)
            return redirect(url_for('medicamentos'))
    if lista == "ENFERMEDADES":
        objeto = buscarPorID(text, ENFERMEDADES)
        if request.method == 'POST':
            nombre=request.form['nombre']
            descripcion=request.form['descripcion']
            foto=request.form['foto']
            modificarObjeto(objeto,LISTAS,nombre=nombre,descripcion=descripcion,foto=foto)
            return redirect(url_for('enfermedad'))
    if lista== "USERS":
        objeto=buscarPorID(text, USERS)
        if request.method == 'POST':
            if request.form['tipo']== "Admin" or "admin" or request.form['tipo']=="User" or "user":
                username=request.form['username']
                nombre=request.form['nombre']
                admin= 1 if request.form['tipo'] == "Admin" or "admin" else 0
                foto= request.form['foto']
                modificarObjeto(objeto,LISTAS,username=username,nombre=nombre,admin=admin,foto=foto)
                return redirect(url_for('usuarios'))
            else:
                return redirect(url_for('usuarios'))
    if lista == "DOSIS":
        objeto = buscarPorID(text, DOSIS)
        if request.method == 'POST':
            if verificarPorID(request.form['animal'],ANIMALES)==False:
                error="El animal no existe"
            elif verificarPorID(request.form['medicamentos'],MEDICAMENTOS)==False:
                error="El medicamento no existe"
            elif verificarPorID(request.form['enfermedad'],ENFERMEDADES)==False:
                error="La enfermedad no existe"
            else:
                id=request.form['id']
                animal=request.form['animal']
                medicamentos=request.form['medicamentos']
                enfermedad=request.form['enfermedad']
                rangopeso=request.form['rangopeso']
                dosis=request.form['dosis']
                modificarObjeto(objeto, LISTAS, id=id, animal=animal, medicamentos=medicamentos,enfermedad=enfermedad,rangoPeso=rangopeso,dosis=dosis)
                return redirect(url_for('dosis_Enfermedad'))
    if lista=="PRESCRIPCIONES":
        objeto = buscarPorID(text, PRESCRIPCIONES)
        if request.method == 'POST':
            if verificarPorID(request.form['usuario'],USERS)==False:
                error="El usuario no existe"
            elif verificarPorID(request.form['animal'],ANIMALES)==False:
                error="El animal no existe"
            elif verificarPorID(request.form['enfermedad'], ENFERMEDADES) == False:
                error = "La enfermedad no existe"
            elif verificarPorID(request.form['dosis'],DOSIS)==False:
                error="La dosis no existe"
            else:
                id = request.form['id']
                usuario=request.form['usuario']
                animal = request.form['animal']
                enfermedad = request.form['enfermedad']
                peso = request.form['peso']
                dosis = request.form['dosis']
                modificarObjeto(objeto, LISTAS, id=id, usuario=usuario,animal=animal, enfermedad=enfermedad, peso=peso, dosis=dosis)
                return redirect(url_for('prescripcion'))

    return render_template('modificar.html',a=objeto,user=sesion,lista=lista,error=error)

@app.route('/medicamentos',methods=['GET','POST'])
def medicamentos():
    if request.method == 'POST':
        Consulta=request.form['text']

    page = request.args.get('page', type=int, default=1)
    global sesion
    filtro = filtrarEliminados(MEDICAMENTOS)
    a = dividir(filtro, 5)
    if (len(a) > 0):
        medicacion = a[page - 1]
    else:
        medicacion = []
    pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='Medicinas')
    if request.method == 'POST':
        if request.form['text']=="":
            return redirect(url_for('medicamentos'))
        medicacion=[buscarPorID(request.form['text'],MEDICAMENTOS)]
        pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='Medicinas')



    return render_template('medicamentos.html',
                           medicacion=medicacion,
                           pagination=pagination,user=sesion
                           )
@app.route('/medicamentos/<text>',methods=['GET','POST'])
def medicamentos1(text):
    page = request.args.get('page', type=int, default=1)
    global sesion
    filtro = filtrarEliminados(MEDICAMENTOS)
    medicamentos = [buscarPorID(text, filtrarEliminados(filtro))]
    pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='enfermedad')
    return render_template('medicamentos.html',
                           medicacion=medicamentos,
                           pagination=pagination,text=text,user=sesion)
@app.route('/prescripcion',methods=['GET','POST'])
def prescripcion():
    if request.method == 'POST':
        Consulta=request.form['text']

    page = request.args.get('page', type=int, default=1)
    filtro=filtrarEliminados(PRESCRIPCIONES)
    a=dividir(filtro,5)
    if(len(a)>0):
        prescrip =a[page-1]
    else: prescrip=[]
    pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='Prescripcion')
    if request.method == 'POST':
        if request.form['text']=="":
            return redirect(url_for('prescripcion'))
        prescrip=[buscarPorID(request.form['text'],filtro)]
        pagination = Pagination(page=page, per_page=5 , total=len(filtro),  record_name='prescrip')

    global sesion
    return render_template('prescripciones.html',
                           prescrip=prescrip,
                           pagination=pagination,user=sesion
                           )


@app.route('/usuarios',methods=['GET','POST'])
def usuarios():

    page = request.args.get('page', type=int, default=1)
    filtro=filtrarEliminados(USERS)
    a=dividir(filtro,5)
    if(len(a)>0):
        user =a[page-1]
    else: user=[]
    global sesion
    pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='user')
    if request.method == 'POST':
        if request.form['text'] == "":
            return redirect(url_for('usuarios'))
        user = [buscarPorID(request.form['text'], USERS)]
        pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='user')

    return render_template('users.html',
                           user1=user,
                           pagination=pagination,user=sesion
                           )

@app.route('/usuarios/<text>',methods=['GET','POST'])
def usuarios1(text):
    global sesion
    page = request.args.get('page', type=int, default=1)
    user = [buscarPorID(text, USERS)]
    pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(user)), total=len(user), record_name='usuarios')
    return render_template('users.html',
                           user1=user,
                           pagination=pagination,text=text,user=sesion
                           )

@app.route('/insertar/<text>',methods=['GET','POST'])
def insertar(text):
    error=None
    info=""
    global sesion
    if text=="USERS":
        info="usuarios"
        username = ""
        password = ""
        nombre = ""
        foto = ""
        if request.method == 'POST':
            if verificarPorID(request.form['username'], USERS):
                error = "El Usuario ya esta registrado"
            elif request.form['username'] == "" or request.form['password'] == "" or request.form['nombre'] == "":
                error = "Faltan campos sin completar"

            else:
                foto = "http://www.getsmartcontent.com/content/uploads/2014/08/shutterstock_149293433.jpg" if request.form['foto'] == "" else request.form['foto']
                username = request.form['username']
                password = request.form['password']
                nombre = request.form['nombre']
                insertarObjeto(Usuario(), USERS, username=username, nombre=nombre, passw=password, foto=foto, admin=0, nombreTabla="usuario")
                error = "Registro Completado"
    if text=="MEDICAMENTOS":
        info="medicamentos"
        nombre = ""
        descripcion = ""
        foto = ""
        if request.method == 'POST':
            if verificarPorID(request.form['nombre'], MEDICAMENTOS):
                error = "El Medicamento ya esta registrado"
            elif request.form['nombre'] == "" or request.form['Descripcion'] == "":
                error = "Faltan campos sin completar"

            else:
                foto = "http://www.getsmartcontent.com/content/uploads/2014/08/shutterstock_149293433.jpg" if request.form['foto'] == "" else request.form['foto']
                nombre = request.form['nombre']
                descripcion = request.form['Descripcion']
                insertarObjeto(Medicamento(), MEDICAMENTOS, nombre=nombre, descripcion=descripcion, foto=foto, nombreTabla="medicamentos")
                error = "Registro Completado"
    if text=="ENFERMEDADES":
        info="enfermedades"
        nombre = ""
        descripcion = ""
        foto = ""
        if request.method == 'POST':
            if verificarPorID(request.form['nombre'], ENFERMEDADES):
                error = "El Enfermedad ya esta registrado"
            elif request.form['nombre'] == "" or request.form['Descripcion'] == "":
                error = "Faltan campos sin completar"

            else:
                foto = "http://www.getsmartcontent.com/content/uploads/2014/08/shutterstock_149293433.jpg" if request.form['foto'] == "" else request.form['foto']
                nombre = request.form['nombre']
                descripcion = request.form['Descripcion']
                insertarObjeto(Enfermedad(), ENFERMEDADES, nombre=nombre, descripcion=descripcion, foto=foto, nombreTabla="enfermedad")
                error = "Registro Completado"
    if text=="ANIMALES":
        info="animales"
        nombre = ""
        descripcion = ""
        foto = ""
        if request.method == 'POST':
            if verificarPorID(request.form['nombre'], ANIMALES):
                error = "El animal ya esta registrado"
            elif request.form['nombre'] == "" or request.form['Descripcion'] == "":
                error = "Faltan campos de completar"

            else:
                foto = "http://www.getsmartcontent.com/content/uploads/2014/08/shutterstock_149293433.jpg" if request.form['foto'] == "" else request.form['foto']
                nombre = request.form['nombre']
                descripcion = request.form['Descripcion']
                insertarObjeto(Animal(), ANIMALES, nombre=nombre, descripcion=descripcion, foto=foto, nombreTabla="animal")
                error = "Registro Completado"

    if text=="PRESCRIPCIONES":
        info="prescripciones"
        id=""
        animal=""
        enfermedad=""
        peso=""
        dosis=""
        if request.method == 'POST':
            if request.form['id'] =="" or request.form['animal'] =="" or request.form['enfermedad']=="" or request.form['peso']=="" or request.form['dosis']=="":
                error = "Faltan campos de completar"
            elif verificarPorID(request.form['id'],PRESCRIPCIONES):
                error="La prescripcion ya esta registrada"
            elif verificarPorID(request.form['animal'],ANIMALES) == False:
                error= "El animal no existe"
            elif verificarPorID(request.form['enfermedad'],ENFERMEDADES)==False:
                error="Enfermedad no existe"
            elif verificarPorID(request.form['dosis'],DOSIS)==False:
                error="Dosis no encontrada"
            else:
                id=request.form['id']
                animal = request.form['animal']
                enfermedad = request.form['enfermedad']
                peso = request.form['peso']
                dosis = request.form['dosis']
                insertarObjeto(Prescripcion(), PRESCRIPCIONES, id=id, usuario=sesion.getID(),animal=animal, enfermedad=enfermedad,peso=peso,dosis=dosis, nombreTabla="prescripcion")
                error = "Registro Completado"
    if text=="DOSIS":
        info="dosis"
        id=""
        animal=""
        medicamento=""
        enfermedad=""
        rangoPeso=""
        dosis=""
        if request.method == 'POST':
            if request.form['id'] =="" or request.form['animal'] =="" or request.form['medicamento']=="" or request.form['enfermedad']=="" or request.form['rangoPeso']=="" or request.form['dosis']=="":
                error = "Faltan campos de completar"
            elif verificarPorID(request.form['id'],DOSIS):
                error="La dosis ya esta registrada"
            elif verificarPorID(request.form['animal'],ANIMALES) == False:
                error= "El animal no existe"
            elif verificarPorID(request.form['medicamento'],MEDICAMENTOS) == False:
                error= "El medicamento no existe"
            elif verificarPorID(request.form['enfermedad'], ENFERMEDADES) == False:
                error = "Enfermedad no existe"
            else:
                id = request.form['id']
                animal = request.form['animal']
                medicamento = request.form['medicamento']
                enfermedad = request.form['enfermedad']
                rangoPeso = request.form['rangoPeso']
                dosis = request.form['dosis']
                insertarObjeto(Dosis(), DOSIS, id=id, animal=animal, enfermedad=enfermedad,medicamento=medicamento, rangoPeso=rangoPeso, dosis=dosis, nombreTabla="dosis")
                error = "Registro Completado"

    return render_template('insertar.html',error=error,text=text,user=sesion,info=info)





@app.route('/dosis_Enfermedad',methods=['GET','POST'])
def dosis_Enfermedad():

    if request.method == 'POST':
        Consulta = request.form['text']

    page = request.args.get('page', type=int, default=1)
    global sesion
    filtro = filtrarEliminados(DOSIS)
    a = dividir(filtro, 5)
    if (len(a) > 0):
        dosis = a[page - 1]
    else:
        dosis = []
    pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='DOSIS')
    if request.method == 'POST':
        if request.form['text'] == "" and request.form['submit']=="Enfermedad":
            return redirect(url_for('dosis_Enfermedad'))
        if request.form['animal'] == "" and request.form['submit']=="Animal":
            return redirect(url_for('dosis_Enfermedad'))
        if request.form['id'] == "" and request.form['submit']=="ID":
            return redirect(url_for('dosis_Enfermedad'))
        if request.form['text'] != "" and request.form['submit']=="Enfermedad":
            return redirect(url_for('dosis_Enfermedad2',tipo='Enfermedad',text=request.form['text']))

        if request.form['animal'] != "" and request.form['submit']=="Animal":
            return redirect(url_for('dosis_Enfermedad2', tipo='Animal', text=request.form['animal']))

        if request.form['id'] != "" and request.form['submit']=="ID":
            dosis = [buscarPorID(request.form['id'], filtro)]
            pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='dosis')
    return render_template('dosis.html',
                           dosis=dosis,
                           pagination=pagination,variable="dosis_Enfermedad",user=sesion
                           )

@app.route('/dosis_Enfermedad/<text>',methods=['GET','POST'])
def dosis_Enfermedad1(text):
    page = request.args.get('page', type=int, default=1)
    global sesion
    filtro = filtrarEliminados(DOSIS)
    dosis = [buscarPorID(text, filtrarEliminados(filtro))]
    pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='enfermedad')
    return render_template('dosis.html',
                           dosis=dosis,
                           pagination=pagination,text=text,user=sesion)

@app.route('/dosis_Enfermedad/<tipo>/<text>',methods=['GET','POST'])
def dosis_Enfermedad2(tipo,text):
    page = request.args.get('page', type=int, default=1)
    global sesion
    if tipo=="Enfermedad":
        filtro = filtrarEliminados(dosisEnfermedad(text, DOSIS))
        a = dividir(filtro, 5)
        if (len(a) > 0):
            dosis = a[page - 1]
        else:
            dosis = []
        pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='enfermedad')
    else:
        filtro = filtrarEliminados(dosisAnimal(text, DOSIS))
        a = dividir(filtro, 5)
        if (len(a) > 0):
            dosis = a[page - 1]
        else:
            dosis = []
        pagination = Pagination(page=page, per_page=5, total=len(filtro), record_name='enfermedad')
    return render_template('dosis.html',
                           dosis=dosis,
                           pagination=pagination,user=sesion,text=text)