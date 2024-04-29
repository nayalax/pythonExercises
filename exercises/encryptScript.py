from EncryptNameClass import EncryptName

encryptName = EncryptName()

nombre_anonimizado = encryptName.hash_first_last("Nicholas", "Ayala")
nombre_anonimizado_md5 = encryptName.hash_md5first_last("Nicholas", "Ayala")
print(nombre_anonimizado) # Muestra el hash del nombre "Nicholas Ayala"
print(nombre_anonimizado_md5)

############################################################################################


# Cifrar un nombre
name_encrypted = encryptName.encrypt_name("Nicholas", "Ayala")
print("Nombre Cifrado:", name_encrypted)
# Descifrar el nombre
name_decrypted = encryptName.decrypt_name(name_encrypted)
print("Nombre Descifrado:", name_decrypted)