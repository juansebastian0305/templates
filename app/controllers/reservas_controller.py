from flask import render_template, request, redirect, url_for
from app import app
from app.models.reservas import Reserva, reservas_db
from app.models.cliente import clientes_db
from app.models.habitacion import habitaciones_db

@app.route('/reservas')
def listar_reservas():
    return render_template('reservas/list.html', reservas=reservas_db, clientes=clientes_db, habitaciones=habitaciones_db)

@app.route('/reservas/create', methods=['GET', 'POST'])
def crear_reserva():
    if request.method == 'POST':
        cliente_id = int(request.form['cliente_id'])
        cliente = next(c for c in clientes_db if c.id == cliente_id)
        aplica_iva = cliente.tipo_cliente == 'nacional'

        nueva = Reserva(
            id=len(reservas_db) + 1,
            cliente_id=cliente_id,
            habitacion_id=int(request.form['habitacion_id']),
            motivo=request.form['motivo'],
            fecha_inicio=request.form['fecha_inicio'],
            fecha_fin=request.form['fecha_fin'],
            precio=float(request.form['precio']),
            aplica_iva=aplica_iva
        )
        reservas_db.append(nueva)
        return redirect(url_for('listar_reservas'))
    
    return render_template('reservas/create.html', clientes=clientes_db, habitaciones=habitaciones_db)

@app.route('/reservas/edit/<int:id>', methods=['GET', 'POST'])
def editar_reserva(id):
    reserva = next((r for r in reservas_db if r.id == id), None)
    if request.method == 'POST':
        cliente_id = int(request.form['cliente_id'])
        cliente = next(c for c in clientes_db if c.id == cliente_id)
        reserva.cliente_id = cliente_id
        reserva.habitacion_id = int(request.form['habitacion_id'])
        reserva.motivo = request.form['motivo']
        reserva.fecha_inicio = request.form['fecha_inicio']
        reserva.fecha_fin = request.form['fecha_fin']
        reserva.precio = float(request.form['precio'])
        reserva.aplica_iva = cliente.tipo_cliente == 'nacional'
        return redirect(url_for('listar_reservas'))
    return render_template('reservas/edit.html', reserva=reserva, clientes=clientes_db, habitaciones=habitaciones_db)
