from flask import render_template, request, redirect, url_for
from app import app
from app.models.habitacion import Habitacion, habitaciones_db
from app.models.hotel import hoteles_db  # para obtener lista de hoteles

@app.route('/habitaciones')
def listar_habitaciones():
    return render_template('habitaciones/list.html', habitaciones=habitaciones_db)

@app.route('/habitaciones/create', methods=['GET', 'POST'])
def crear_habitacion():
    if request.method == 'POST':
        nueva = Habitacion(
            id=len(habitaciones_db) + 1,
            numero=request.form['numero'],
            piso=request.form['piso'],
            tipo=request.form['tipo'],
            estado=request.form['estado'],
            hotel_id=request.form['hotel_id']
        )
        habitaciones_db.append(nueva)
        return redirect(url_for('listar_habitaciones'))
    return render_template('habitaciones/create.html', hoteles=hoteles_db)

@app.route('/habitaciones/edit/<int:id>', methods=['GET', 'POST'])
def editar_habitacion(id):
    habitacion = next((h for h in habitaciones_db if h.id == id), None)
    if request.method == 'POST':
        habitacion.numero = request.form['numero']
        habitacion.piso = request.form['piso']
        habitacion.tipo = request.form['tipo']
        habitacion.estado = request.form['estado']
        habitacion.hotel_id = request.form['hotel_id']
        return redirect(url_for('listar_habitaciones'))
    return render_template('habitaciones/edit.html', habitacion=habitacion, hoteles=hoteles_db)
