import string
from . import passgen
from importlib.metadata import version

__version__ = version("pypasskit") 
__all__ = ["generate", "entropy"]

def generate(length=6):
    pincode= passgen.generate(upper=False, lower=False, numbers=True, symbols=False, length=length, returnPool=False)
    return pincode
    
def entropy(length=6):
    if not(isinstance(length, int)):
        raise TypeError(f"[236] (pingen@PPK v{__version__}) - PIN length must be given as an integer.")
    
    if length < 1:
        raise ValueError(f"[237] (pingen@PPK v{__version__}) - Length must be greater than or equal to 1 for a PIN.")
    entropy = passgen.entropy(pool=string.digits, length=length)
    return entropy
