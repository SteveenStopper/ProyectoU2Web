#Permite acceder a las funcionalidades del sistema operativo
import os
#Import flask library
from flask import Flask, render_template, request, flash, redirect, url_for
#Importacion libreria para la coneccion con MongoDb
import pymongo

#Iniciar variable de aplicacion 
app = Flask(__name__)
app.debug = False
#Instanciamiento de la carpeta Static para acceder 
app._static_folder = os.path.abspath("templates/static/")

# Secret key for session
app.secret_key = 'mysecretkey'

#Conexion con MongoDb
MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

MONGO_BASEDATOS="dbProyectoU2"
MONGO_COLLECTION_MAESTRO="Maestro"
MONGO_COLLECTION_MATERIA="Materia"
MONGO_COLLECTION_NOTAS="Notas"
MONGO_COLLECTION_ALUMNO="Alumno"
cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos=cliente[MONGO_BASEDATOS]
coleccionMaestro=baseDatos[MONGO_COLLECTION_MAESTRO]
#return a list of all collections in your database
print(baseDatos.list_collection_names())


#ruta principal 
@app.route("/")
#Función principal que llamará a la página HTML
def principal():
    return render_template("layouts/index.html")

#Metodo para obtener los datos de un niño al loguerse

#Ruta Login Docente
@app.route('/Login_Docente')
#Funcion de ingreso a la pagina Login de Docente
def Login_Docente():
    return render_template('layouts/Login_Docente.html')

@app.route('/login', methods=['POST'])
def login():
    if(request.method == "POST"): 
        #Instanciamiento de deatos de la pagina de Login
        correo = request.form['email']          
        contrasenia = request.form['password']       
        try:
            user = coleccionMaestro.find_one({'email':correo,'clave':contrasenia})
            if(user):
                return render_template('layouts/Tabla_Alumnos.html')
            else:
                flash('Usuario no registrado', 'danger')
                return render_template('layouts/Login_Docente.html')
        except:
            return render_template('layouts/serverError.html')
      

#Ruta de tabla de alumnos
@app.route('/Tabla_Alumnos')
#Funcion de ingreso a la pagina tabla de alumnos
def Tabla_Alumnos():
    return render_template('layouts/Tabla_Alumnos.html')

#Ruta Juego de pares
@app.route('/JuegoPares', methods=['GET'])
#Funcion de ingreso a la pagina del juego
def JuegoPares():
    print(request.args.get('nombre'))
    return render_template('layouts/Juego_Memoria.html', nombre= request.args.get('nombre'))


# main del programa 
if __name__ == "__main__":
    #debug = true, para reiniciar automaticamente el servidor, tiempo de desarrollo
    app.run(debug=True) # Para ejecutar la aplicacion