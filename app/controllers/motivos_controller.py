from flask import render_template, request, redirect, url_for
from app import app
from app.models.motivos import Motivo, motivos_db

@app.route('/motivos')
def listar_motivos():
    return render_template('motivos/list.html', motivos=motivos_db)

@app.route('/motivos/create', methods=['GET', 'POST'])
def crear_motivo():
    if request.method == 'POST':
        nuevo = Motivo(id=len(motivos_db)+1, nombre=request.form['nombre'])
        motivos_db.append(nuevo)
        return redirect(url_for('listar_motivos'))
    return render_template('motivos/create.html')

@app.route('/motivos/edit/<int:id>', methods=['GET', 'POST'])
def editar_motivo(id):
    motivo = next((m for m in motivos_db if m.id == id), None)
    if request.method == 'POST':
        motivo.nombre = request.form['nombre']
        return redirect(url_for('listar_motivos'))
    return render_template('motivos/edit.html', motivo=motivo)
