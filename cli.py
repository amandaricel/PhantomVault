import argparse
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

from phantomvault.crypto import encrypt_file, decrypt_file

# Derive 256-bit key from password
def derive_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


def main():
    parser = argparse.ArgumentParser(description="PhantomVault CLI encryption tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"])
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("password")

    args = parser.parse_args()

    salt = b"phantomvault_salt"
    key = derive_key(args.password, salt)

    if args.mode == "encrypt":
        encrypt_file(args.input, args.output, key)
        print("File encrypted successfully.")

    elif args.mode == "decrypt":
        decrypt_file(args.input, args.output, key)
        print("File decrypted successfully.")


if __name__ == "__main__":
    main()
