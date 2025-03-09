from cryptography.fernet import Fernet

# Load the encryption key (securely store this key outside the project)
ENCRYPTION_KEY = b"your_generated_key_here"  # Use the same key as in encrypt_env.py

# Utility to decrypt environment variables
def decrypt_value(encrypted_value):
    f = Fernet(ENCRYPTION_KEY)
    return f.decrypt(encrypted_value.encode()).decode()

# Decrypt and use the environment variables

