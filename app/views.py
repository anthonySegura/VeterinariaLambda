from app import app
from flask import render_template,request,redirect,url_for
from DataBase.Data import *
from flask_paginate import Pagination
from utilities.Funciones import *

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


@app.route('/usuarios')
def usuarios():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get('page', type=int, default=1)

    user = dividir(USERS, 5)[page - 1]

    pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(USERS)), total=len(USERS), search=search, record_name='Animals')
    if request.method == 'POST':
        if request.form['text'] == "":
            return redirect(url_for('usuarios'))
        user = [buscarPorID(request.form['text'], USERS)]
        pagination = Pagination(page=page, per_page=5, display_msg="Pagina " + str(page) + ". Registros Totales " + str(len(user)), total=len(user), search=search, record_name='Animals')

    return render_template('users.html',
                           user=user,
                           pagination=pagination,
                           )