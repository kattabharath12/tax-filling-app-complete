from cryptography.fernet import Fernet
import os

# For demo purposes - in production, use proper key management
FERNET_KEY = os.getenv("FERNET_KEY", Fernet.generate_key())
fernet = Fernet(FERNET_KEY)

def encrypt_field(value: str) -> str:
    """Encrypt a field value"""
    if not value:
        return value
    return fernet.encrypt(value.encode()).decode()

def decrypt_field(token: str) -> str:
    """Decrypt a field value"""
    if not token:
        return token
    return fernet.decrypt(token.encode()).decode()
