import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Encrypt file using AES-256
def encrypt_file(input_file, output_file, key):
    iv = os.urandom(16)
    cipher = Cipher(
        algorithms.AES(key),
        modes.CFB(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()

    with open(input_file, "rb") as f:
        data = f.read()

    encrypted = encryptor.update(data) + encryptor.finalize()

    with open(output_file, "wb") as f:
        f.write(iv + encrypted)


# Decrypt file using AES-256
def decrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = Cipher(
        algorithms.AES(key),
        modes.CFB(iv),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()

    decrypted = decryptor.update(encrypted_data) + decryptor.finalize()

    with open(output_file, "wb") as f:
        f.write(decrypted)
