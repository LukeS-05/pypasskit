import secrets, string, math
from . import passgen

version = "0.6.1"
__all__ = ["generate", "entropy"]

def generate(length=6):
    pincode = passgen.generate(upper=False, lower=False, numbers=True, symbols=False, length=length)
    return pincode
    
def entropy(length=0):
    entropy = passgen.entropy(string.digits, length)
    return entropy
