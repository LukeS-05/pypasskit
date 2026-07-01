import secrets

version = "0.7.0"
def hexToken(numbytes=16):
    try:
        token = secrets.token_hex(numbytes)
        return token
    except TypeError as e:
        raise TypeError(f"[221] (PPK v{version}) - numbytes must be given as an integer. {e}") from None

def webToken(numbytes=32):
    try:
        token = secrets.token_urlsafe(numbytes)
        return token
    except TypeError as e:
        raise TypeError(f"[221] (PPK v{version}) - numbytes must be given as an integer. {e}") from None