from fastapi import FastAPI, HTTPException, Query
from models import Cliente, Factura, ClienteUpdate, FacturaUpdate
from typing import List
import re

if __name__ == "__main__":
    ...

app = FastAPI()

# Diccionarios simulados para almacenar datos
clientes = {}
facturas = {}

# CRUD para Clientes
@app.post("/clientes/")
def crear_cliente(cliente: Cliente):
    if cliente.id_cliente in clientes:
        raise HTTPException(status_code=409, detail="Cliente ya existe")
    clientes[cliente.id_cliente] = cliente
    return cliente

@app.get("/clientes/{id_cliente}")
def obtener_cliente(id_cliente: int):
    if id_cliente not in clientes:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return clientes[id_cliente]

@app.put("/clientes/{id_cliente}")
def actualizar_cliente(id_cliente: int, cliente: Cliente):
    if id_cliente not in clientes:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    clientes[id_cliente] = cliente
    return cliente

@app.patch("/clientes/{id_cliente}")
def actualizar_cliente_parcialmente(id_cliente: int, update: ClienteUpdate):
    if id_cliente not in clientes:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    cliente_actual = clientes[id_cliente]
    update_data = update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cliente_actual, key, value)
    clientes[id_cliente] = cliente_actual
    return cliente_actual

@app.get("/clientes/buscar/", response_model=List[Cliente])
def buscar_clientes(texto: str = Query(None, min_length=3)):
    """
    Busca clientes que coincidan con el texto proporcionado en sus nombres o apellidos.
    El parámetro 'texto' debe tener al menos 3 caracteres para realizar la búsqueda.
    """
    if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ ]+$", texto):
        raise HTTPException(status_code=400, detail="El texto de búsqueda debe contener solo caracteres alfabéticos")
    resultados = []
    
    for _, cliente in clientes.items():
        if texto.lower() in cliente.nombre.lower() or texto.lower() in cliente.apellidos.lower():
            resultados.append(cliente)
    return resultados

@app.delete("/clientes/{id_cliente}")
def borrar_cliente(id_cliente: int):
    if id_cliente not in clientes:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    del clientes[id_cliente]
    return {"message": "Cliente eliminado"}

# CRUD para Facturas
@app.post("/facturas/")
def crear_factura(factura: Factura):
    if factura.id_factura in facturas:
        raise HTTPException(status_code=409, detail="Factura ya existe")
    facturas[factura.id_factura] = factura
    return factura

@app.get("/facturas/{id_factura}")
def obtener_factura(id_factura: int):
    if id_factura not in facturas:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return facturas[id_factura]

@app.put("/facturas/{id_factura}")
def actualizar_factura(id_factura: int, factura: Factura):
    if id_factura not in facturas:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    facturas[id_factura] = factura
    return factura

@app.delete("/facturas/{id_factura}")
def borrar_factura(id_factura: int):
    if id_factura not in facturas:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    del facturas[id_factura]
    return {"message": "Factura eliminada"}

@app.patch("/facturas/{id_factura}")
def actualizar_factura_parcialmente(id_factura: int, update: FacturaUpdate):
    if id_factura not in facturas:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    factura_actual = facturas[id_factura]
    update_data = update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(factura_actual, key, value)
    facturas[id_factura] = factura_actual
    return factura_actual