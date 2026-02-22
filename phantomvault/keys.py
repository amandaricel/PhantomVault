from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate RSA private/public key pair
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096
    )

    public_key = private_key.public_key()

    return private_key, public_key


# Save private key to file
def save_private_key(private_key, filename, password=None):
    encryption = (
        serialization.BestAvailableEncryption(password.encode())
        if password else
        serialization.NoEncryption()
    )

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=encryption
    )

    with open(filename, "wb") as f:
        f.write(pem)


# Save public key to file
def save_public_key(public_key, filename):
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(filename, "wb") as f:
        f.write(pem)
