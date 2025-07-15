from flask import render_template, request, redirect, url_for
from app import app
from app.models.tipohabitacion import TipoHabitacion, tipos_db

@app.route('/tipos')
def listar_tipos():
    return render_template('tipos/list.html', tipos=tipos_db)

@app.route('/tipos/create', methods=['GET', 'POST'])
def crear_tipo():
    if request.method == 'POST':
        nuevo = TipoHabitacion(
            id=len(tipos_db) + 1,
            nombre=request.form['nombre'],
            descripcion=request.form['descripcion']
        )
        tipos_db.append(nuevo)
        return redirect(url_for('listar_tipos'))
    return render_template('tipos/create.html')

@app.route('/tipos/edit/<int:id>', methods=['GET', 'POST'])
def editar_tipo(id):
    tipo = next((t for t in tipos_db if t.id == id), None)
    if request.method == 'POST':
        tipo.nombre = request.form['nombre']
        tipo.descripcion = request.form['descripcion']
        return redirect(url_for('listar_tipos'))
    return render_template('tipos/edit.html', tipo=tipo)
