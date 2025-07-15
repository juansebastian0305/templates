from flask import render_template, request
from app import app
from app.models.reservas import reservas_db
from app.models.cliente import clientes_db

@app.route('/facturas')
def listar_facturas():
    facturas = []
    for r in reservas_db:
        cliente = next((c for c in clientes_db if c.id == r.cliente_id), None)
        subtotal = r.precio
        iva = subtotal * 0.19 if r.aplica_iva else 0
        total = subtotal + iva
        facturas.append({
            "cliente": cliente.nombre if cliente else "Desconocido",
            "precio": subtotal,
            "iva": iva,
            "total": total
        })
    return render_template('facturas/list.html', facturas=facturas)
