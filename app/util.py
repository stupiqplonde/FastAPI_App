import hashlib

def get_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode('utf8')).hexdigest()