from cryptography.fernet import Fernet

def generate_key():
    # Generate a new key for encryption
    key = Fernet.generate_key()
    print(f"Save this key securely: {key.decode()}")
    return key

def encrypt_value(value, key):
    # Encrypt a value using the provided key
    f = Fernet(key)
    encrypted_value = f.encrypt(value.encode())
    print(f"Encrypted value: {encrypted_value.decode()}")
    return encrypted_value

if __name__ == "__main__":
    # Generate a new key or use an existing one
    key = generate_key()
    print(key)
    # key = b"your_generated_key_here"  # Replace with your generated key
    
    # Encrypt sensitive values
    # encrypt_value("your_secret_key", key)
    # encrypt_value("your_db_password", key)
