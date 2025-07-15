from flask import render_template, request, redirect, url_for
from app import app
from app.models.temporada import Temporada, temporadas_db

@app.route('/temporadas')
def listar_temporadas():
    return render_template('temporadas/list.html', temporadas=temporadas_db)

@app.route('/temporadas/create', methods=['GET', 'POST'])
def crear_temporada():
    if request.method == 'POST':
        nueva = Temporada(
            id=len(temporadas_db)+1,
            nombre=request.form['nombre'],
            fecha_inicio=request.form['fecha_inicio'],
            fecha_fin=request.form['fecha_fin']
        )
        temporadas_db.append(nueva)
        return redirect(url_for('listar_temporadas'))
    return render_template('temporadas/create.html')

@app.route('/temporadas/edit/<int:id>', methods=['GET', 'POST'])
def editar_temporada(id):
    temporada = next((t for t in temporadas_db if t.id == id), None)
    if request.method == 'POST':
        temporada.nombre = request.form['nombre']
        temporada.fecha_inicio = request.form['fecha_inicio']
        temporada.fecha_fin = request.form['fecha_fin']
        return redirect(url_for('listar_temporadas'))
    return render_template('temporadas/edit.html', temporada=temporada)
