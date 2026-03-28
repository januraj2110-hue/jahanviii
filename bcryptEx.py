from bcrypt import hashpw, gensalt, checkpw

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return hashpw(password.encode('utf-8'),gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against a hashed value."""
    return checkpw (password.encode('utf-8'), hashed.encode('utf-8')) 
print(hash_password("my_password"))
print(verify_password("my_password", hash_password("my_password")))