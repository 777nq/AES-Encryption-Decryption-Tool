# aes_encryption.py
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def generate_key(password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return salt, key

def encrypt_text(key, text):
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    return encrypted_text

def decrypt_text(key, encrypted_text):
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_text.encode())
    return decrypted_text.decode()

if __name__ == "__main__":
    password = input("Enter your password: ")
    text = input("Enter the text to encrypt: ")

    salt, key = generate_key(password)
    encrypted_text = encrypt_text(key, text)

    print(f"Salt (keep it secret): {base64.urlsafe_b64encode(salt).decode()}")
    print(f"Encrypted Text: {encrypted_text}")

    decrypt = input("Do you want to decrypt this text? (yes/no): ")
    if decrypt.lower() == "yes":
        input_encrypted_text = input("Enter the encrypted text: ")
        decrypted_text = decrypt_text(key, input_encrypted_text)
        print(f"Decrypted Text: {decrypted_text}")
