from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_link(link):
    return cipher_suite.encrypt(link.encode()).decode()

def decrypt_link(encrypted_link):
    return cipher_suite.decrypt(encrypted_link.encode()).decode()
