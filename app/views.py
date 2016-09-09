from app import app
from flask import render_template,request,redirect,url_for

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if  request.method == 'POST':
        if request.form['username']!='admin' or request.form['password']!='admin':
            error='Usuario o contraseña invalidos'
        else:
            return redirect(url_for('marico'))
    return render_template('login.html',error=error)

@app.route('/marico')
def marico():
    return render_template('prueba.html')
