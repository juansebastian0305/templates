from flask import render_template, request, redirect, url_for
from app import app
from app.models.hotel import Hotel, hoteles_db

@app.route('/hoteles')
def listar_hoteles():
    return render_template('hoteles/list.html', hoteles=hoteles_db)

@app.route('/hoteles/create', methods=['GET', 'POST'])
def crear_hotel():
    if request.method == 'POST':
        nuevo = Hotel(
            id=len(hoteles_db)+1,
            nombre=request.form['nombre'],
            direccion=request.form['direccion'],
            telefono=request.form['telefono'],
            categoria=request.form['categoria']
        )
        hoteles_db.append(nuevo)
        return redirect(url_for('listar_hoteles'))
    return render_template('hoteles/create.html')

@app.route('/hoteles/edit/<int:id>', methods=['GET', 'POST'])
def editar_hotel(id):
    hotel = next((h for h in hoteles_db if h.id == id), None)
    if request.method == 'POST':
        hotel.nombre = request.form['nombre']
        hotel.direccion = request.form['direccion']
        hotel.telefono = request.form['telefono']
        hotel.categoria = request.form['categoria']
        return redirect(url_for('listar_hoteles'))
    return render_template('hoteles/edit.html', hotel=hotel)
