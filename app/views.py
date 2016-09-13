from app import app
from flask import render_template,request,redirect,url_for
from DataBase.Data import *
from flask_paginate import Pagination
from utilities.Funciones import *

sesion=None

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if  request.method == 'POST':
        user = list(filter(lambda x: x.username ==str(request.form['username']) and x.passw == str(request.form['password']), USERS))
        if len(user)==0:
            error='Usuario o contraseña invalidos'
        else:
            return redirect(url_for('marico'))
    return render_template('login.html',error=error)



@app.route('/marico',methods=['GET','POST'])
def marico():
    lol="Overwatch"
    if request.method == 'POST':
        if request.form['text']=="hola":
            lol="Pendejo"
    return  render_template('prueba.html', lol=lol)



@app.route('/animals',methods=['GET','POST'])
def animals():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get('page', type=int, default=1)

    animals = dividir(ANIMALES,5)[page-1]

    pagination = Pagination(page=page,per_page=5, display_msg="Pagina "+str(page)+". Registros Totales "+str(len(ANIMALES)),total=len(ANIMALES), search=search, record_name='Animals')
    if request.method == 'POST':
        if request.form['text']=="":
            return redirect(url_for('animals'))
        animals=[buscarPorID(request.form['text'],ANIMALES)]
        pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(animals)), total=len(animals), search=search, record_name='Animals')

    return render_template('animals.html',
                           animals=animals,
                           pagination=pagination,
                           )
@app.route('/animals/<text>',methods=['GET','POST'])
def animals1(text):
    page = request.args.get('page', type=int, default=1)
    animals = [buscarPorID(text, ANIMALES)]
    pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(animals)), total=len(animals), record_name='Animals')
    return render_template('animals.html',
                           animals=animals,
                           pagination=pagination,text=text
                           )
@app.route('/medicamentos',methods=['GET','POST'])
def medicamentos():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    if request.method == 'POST':
        Consulta=request.form['text']

    page = request.args.get('page', type=int, default=1)

    medicacion = dividir(MEDICAMENTOS,5)[page-1]
    pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(MEDICAMENTOS)), total=len(MEDICAMENTOS), search=search, record_name='Medicinas')
    if request.method == 'POST':
        if request.form['text']=="":
            return redirect(url_for('medicamentos'))
        medicacion=[buscarPorID(request.form['text'],MEDICAMENTOS)]
        pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(medicacion)), total=len(medicacion), search=search, record_name='Medicinas')



    return render_template('medicamentos.html',
                           medicacion=medicacion,
                           pagination=pagination,
                           )

@app.route('/prescripcion',methods=['GET','POST'])
def prescripcion():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    if request.method == 'POST':
        Consulta=request.form['text']

    page = request.args.get('page', type=int, default=1)

    prescrip = dividir(PRESCRIPCIONES,5)[page-1]
    pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(PRESCRIPCIONES)), total=len(PRESCRIPCIONES), search=search, record_name='Prescripcion')
    if request.method == 'POST':
        if request.form['text']=="":
            return redirect(url_for('prescripcion'))
        prescrip=[buscarPorID(request.form['text'],PRESCRIPCIONES)]
        pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(prescrip)), total=len(prescrip), search=search, record_name='prescrip')



    return render_template('prescripciones.html',
                           prescrip=prescrip,
                           pagination=pagination,
                           )


@app.route('/usuarios',methods=['GET','POST'])
def usuarios():


    page = request.args.get('page', type=int, default=1)

    user = dividir(USERS, 5)[page - 1]

    pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(USERS)), total=len(USERS), record_name='Animals')
    if request.method == 'POST':
        if request.form['text'] == "":
            return redirect(url_for('usuarios'))
        user = [buscarPorID(request.form['text'], USERS)]
        pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(user)), total=len(user), record_name='Animals')

    return render_template('users.html',
                           user=user,
                           pagination=pagination,
                           )

@app.route('/usuarios/<text>',methods=['GET','POST'])
def usuarios1(text):
    page = request.args.get('page', type=int, default=1)
    user = [buscarPorID(text, USERS)]
    pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(user)), total=len(user), record_name='usuarios')
    return render_template('users.html',
                           user=user,
                           pagination=pagination,text=text
                           )

@app.route('/registroUsuario',methods=['GET','POST'])
def registroUsuario():
    lol=""
    username=""
    password=""
    nombre=""
    foto=""
    if request.method == 'POST':
        if verificarPorID(request.form['username'],USERS):
            lol="El Usuario ya esta registrado"
        elif request.form['username']=="" or request.form['password']=="" or request.form['nombre']=="":
            lol="Faltan campos sin completar"

        else:
            foto="http://www.getsmartcontent.com/content/uploads/2014/08/shutterstock_149293433.jpg" if request.form['foto']=="" else request.form['foto']
            username=request.form['username']
            password=request.form['password']
            nombre=request.form['nombre']
            insertarObjeto(Usuario(), USERS, username = username, nombre = nombre, passw = password, foto = foto, admin = 0,nombreTabla="usuario")
            actualizarBD()
            lol="Registro Completado"
    return render_template('registroUsuario.html',lol=lol)

@app.route('/insertarMedicinas',methods=['GET','POST'])
def insertarMedicina():
    lol = ""
    nombre = ""
    descripcion=""
    foto = ""
    if request.method == 'POST':
        if verificarPorID(request.form['nombre'], MEDICAMENTOS):
            lol = "El Medicamento ya esta registrado"
        elif request.form['nombre'] == "" or request.form['Descripcion'] == "" :
            lol = "Faltan campos sin completar"

        else:
            foto = "http://www.getsmartcontent.com/content/uploads/2014/08/shutterstock_149293433.jpg" if request.form['foto'] == "" else request.form['foto']
            nombre = request.form['nombre']
            descripcion=request.form['Descripcion']
            insertarObjeto(Medicamento(), MEDICAMENTOS, nombre=nombre, descripcion=descripcion,foto=foto,  nombreTabla="medicamentos")
            lol = "Registro Completado"
    return render_template('insertarMedicina.html', lol=lol)

@app.route('/insertarEnfermedad',methods=['GET','POST'])
def insertarEnfermedad():
    lol = ""
    nombre = ""
    descripcion=""
    foto = ""
    if request.method == 'POST':
        if verificarPorID(request.form['nombre'], MEDICAMENTOS):
            lol = "El Enfermedad ya esta registrado"
        elif request.form['nombre'] == "" or request.form['Descripcion'] == "" :
            lol = "Faltan campos sin completar"

        else:
            foto = "http://www.getsmartcontent.com/content/uploads/2014/08/shutterstock_149293433.jpg" if request.form['foto'] == "" else request.form['foto']
            nombre = request.form['nombre']
            descripcion=request.form['Descripcion']
            insertarObjeto(Enfermedad(), ENFERMEDADES, nombre=nombre, descripcion=descripcion,foto=foto,  nombreTabla="enfermedad")
            lol = "Registro Completado"
    return render_template('insertarMedicina.html', lol=lol)
