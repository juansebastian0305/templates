from flask import render_template, redirect, url_for, request, session
from app import app
from app.controllers import hotel_controller
from app.controllers import categoria_controller
from app.controllers import habitacion_controller
from app.controllers import cliente_controller
from app.controllers import reservas_controller
from app.controllers import motivos_controller
from app.controllers import temporada_controller
from app.controllers import tipohabitacion_controller
from app.controllers import factura_controller



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Ejemplo de usuario y contraseña, reemplaza con tu lógica de base de datos
        if username == 'admin' and password == 'admin':
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Usuario o contraseña incorrectos'
    return render_template('login.html', error=error)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')