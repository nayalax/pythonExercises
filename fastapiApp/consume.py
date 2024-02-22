import requests

BASE_URL = "http://127.0.0.1:8080"  # Ajusta según la URL de tu API FastAPI

def crear_cliente(cliente_data):
    response = requests.post(f"{BASE_URL}/clientes/", json=cliente_data)
    print("Crear Cliente:", response.json())

def obtener_cliente(id_cliente):
    response = requests.get(f"{BASE_URL}/clientes/{id_cliente}")
    print("Obtener Cliente:", response.json())

def actualizar_cliente(id_cliente, cliente_data):
    response = requests.put(f"{BASE_URL}/clientes/{id_cliente}", json=cliente_data)
    print("Actualizar Cliente:", response.json())

def borrar_cliente(id_cliente):
    response = requests.delete(f"{BASE_URL}/clientes/{id_cliente}")
    print("Borrar Cliente:", response.status_code, response.json())

def crear_factura(factura_data):
    response = requests.post(f"{BASE_URL}/facturas/", json=factura_data)
    print("Crear Factura:", response.json())

def obtener_factura(id_factura):
    response = requests.get(f"{BASE_URL}/facturas/{id_factura}")
    print("Obtener Factura:", response.json())

def actualizar_factura(id_factura, factura_data):
    response = requests.put(f"{BASE_URL}/facturas/{id_factura}", json=factura_data)
    print("Actualizar Factura:", response.json())

def borrar_factura(id_factura):
    response = requests.delete(f"{BASE_URL}/facturas/{id_factura}")
    print("Borrar Factura:", response.status_code, response.json())

if __name__ == "__main__":
    # Datos de ejemplo basados en los modelos Pydantic proporcionados
    cliente_data = {
        "nombre": "Natalia",
        "apellidos": "García",
        "id_fiscal": "A1453678",
        "id_cliente": 19
    }

    factura_data = {
        "id_factura": 23,
        "concepto": "Compra de material de oficina",
        "cliente": {
            "nombre": "Natalia",
            "apellidos": "García",
            "id_fiscal": "A1453678",
            "id_cliente": 19
        },
        "importe": 123.45
    }

    crear_cliente(cliente_data)
    obtener_cliente(19)
    actualizar_cliente(19, {**cliente_data, "nombre": "Ana María"})
    
    crear_factura(factura_data)
    obtener_factura(23)
    actualizar_factura(23, {**factura_data, "importe": 200.00})
   
