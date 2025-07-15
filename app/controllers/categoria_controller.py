from flask import render_template, request, redirect, url_for
from app import app
from app.models.categoria import Categoria, categorias_db

@app.route('/categorias')
def listar_categorias():
    return render_template('categorias/list.html', categorias=categorias_db)

@app.route('/categorias/create', methods=['GET', 'POST'])
def crear_categoria():
    if request.method == 'POST':
        nueva = Categoria(id=len(categorias_db)+1, nombre=request.form['nombre'])
        categorias_db.append(nueva)
        return redirect(url_for('listar_categorias'))
    return render_template('categorias/create.html')

@app.route('/categorias/edit/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    categoria = next((c for c in categorias_db if c.id == id), None)
    if request.method == 'POST':
        categoria.nombre = request.form['nombre']
        return redirect(url_for('listar_categorias'))
    return render_template('categorias/edit.html', categoria=categoria)
