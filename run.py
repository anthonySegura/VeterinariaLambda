from app import app
from DataBase.Data import *

cargarDatos()

app.run(debug=True,port=8080)
