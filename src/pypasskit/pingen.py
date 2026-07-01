import secrets, string, math
from . import passgen

version = "0.7.0"
__all__ = ["generate", "entropy"]

def generate(length=6):
    pincode = passgen.generate(upper=False, lower=False, numbers=True, symbols=False, length=length)
    return pincode
    
def entropy(length=0):
    if not(isinstance(length, int)):
        raise TypeError(f"[226] (PPK v{version}) - PIN length must be given as an integer.")
    
    if length < 1:
        raise ValueError(f"[227] (PPK v{version}) - Length must be greater than or equal to 1 for a PIN.")
    entropy = passgen.entropy(upper=False, lower=False, numbers=True, symbols=False, length=length)
    return entropy
