from pydantic import BaseModel, validator
from decimal import Decimal
from typing import Optional, List
import re

class Persona(BaseModel):
    # Validador personalizado para el nombre y apellidos
    @validator('nombre', 'apellidos', pre=True, each_item=False)
    def solo_caracteres_alfabeticos(cls, v):
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ ]+$", v):
            raise ValueError('Debe contener solo caracteres alfabéticos')
        return v
    @validator('id_fiscal', pre=True, each_item=False)
    def solo_caracteres_alfanumericos(cls, v):
        if not re.match("^[0-9A-Z]+$", v):
            raise ValueError('El valor debe contener solo letras mayúsculas y números.')
        return v
    nombre: str
    apellidos: str
    id_fiscal: str

class Cliente(Persona):
    id_cliente: int

class Factura(BaseModel):
    id_factura: int
    concepto: str
    cliente: Cliente
    importe: Decimal

class ClienteUpdate(BaseModel):
    @validator('nombre', 'apellidos', pre=True, each_item=False)
    def solo_caracteres_alfabeticos(cls, v):
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ ]+$", v):
            raise ValueError('Debe contener solo caracteres alfabéticos')
        return v
    @validator('id_fiscal', pre=True, each_item=False)
    def solo_caracteres_alfanumericos(cls, v):
        if not re.match("^[0-9A-Z]+$", v):
            raise ValueError('Debe contener solo caracteres alfanuméricos')
        return v
    nombre: Optional[str] = None
    apellidos: Optional[str] = None
    id_fiscal: Optional[str] = None
    
class FacturaUpdate(BaseModel):
    concepto: Optional[str] = None
    importe: Optional[Decimal] = None