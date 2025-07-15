from flask import render_template, request, redirect, url_for
from app import app
from app.models.cliente import Cliente, clientes_db

@app.route('/clientes')
def listar_clientes():
    return render_template('clientes/list.html', clientes=clientes_db)

@app.route('/clientes/create', methods=['GET', 'POST'])
def crear_cliente():
    if request.method == 'POST':
        nuevo = Cliente(
            id=len(clientes_db) + 1,
            nombre=request.form['nombre'],
            documento=request.form['documento'],
            tipo_cliente=request.form['tipo_cliente'],
            es_agencia=(request.form.get('es_agencia') == 'on')
        )
        clientes_db.append(nuevo)
        return redirect(url_for('listar_clientes'))
    return render_template('clientes/create.html')

@app.route('/clientes/edit/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = next((c for c in clientes_db if c.id == id), None)
    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.documento = request.form['documento']
        cliente.tipo_cliente = request.form['tipo_cliente']
        cliente.es_agencia = (request.form.get('es_agencia') == 'on')
        return redirect(url_for('listar_clientes'))
    return render_template('clientes/edit.html', cliente=cliente)
