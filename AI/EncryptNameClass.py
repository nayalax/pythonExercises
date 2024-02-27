import hashlib as hash
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class EncryptName:
    def __init__(self):
        self.key = self.generate_key()
        
    def generate_key(self):
        return Fernet.generate_key()
        
    def hash_first_last (self, firstName, lastName):
        # Concatenar nombre y apellido
        fullName = firstName + " " + lastName
        # Codificar el nombre completo para prepararlo para el hashing
        encoded_name = fullName.encode()
        # Crear el hash usando SHA-256
        hash_object = hash.sha256(encoded_name)
        # Obtener el valor hash hexadecimal
        hash_hex = hash_object.hexdigest()
        return hash_hex
    
    def hash_md5first_last(self, firstName, lastName):
        # Concatenar nombre y apellido
        fullName = firstName + " " + lastName
        # Codificar el nombre completo para prepararlo para el hashing
        encoded_name = fullName.encode()
        # md5
        hash_objeto_md5 = hash.md5(encoded_name)
        # Obtener el valor hash hexadecimal
        hash_hex = hash_objeto_md5.hexdigest()
        return hash_hex
    
    def encrypt_name(self, firstName, lastName ):
        name = firstName + " " + lastName
        # Crear una instancia de Fernet con la clave proporcionada
        f = Fernet(self.key)
        # Codificar el nombre y cifrarlo
        encoded_name = name.encode()
        encrypted_name = f.encrypt(encoded_name)
        return encrypted_name
    
    def decrypt_name(self, encrypted_name):
        # Crear una instancia de Fernet con la clave proporcionada
        f = Fernet(self.key)
        # Descifrar y decodificar el nombre
        name_decrypted = f.decrypt(encrypted_name)
        original_name = name_decrypted.decode()
        return original_name