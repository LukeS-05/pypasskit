#  ____  ____  _  __   To learn more about the PyPassKit source code, please go to
# |  _ \|  _ \| |/ /   https://lukes-05.github.io/pypasskit/source
# | |_) | |_) | ' /    
# |  __/|  __/| . \    Copyright (C) 2026 LukeS-05 - This library is licensed under the 
# |_|   |_|   |_|\_\   MIT License 
# ______________________________________________________________________________________

import secrets, string, math
from importlib.metadata import version

__version__ = version("pypasskit") 
__all__ = ["generate", "buildPool", "entropy"]

def buildPool(upper=True, lower=True, numbers=True, symbols=True):
    # 1 - CHECK BOOLEAN VALUES HAVE BEEN PASSED
    if not(isinstance(upper, bool)) or not(isinstance(lower, bool)) or not(isinstance(numbers, bool)) or not(isinstance(symbols, bool)):
        raise TypeError(f"[201] (passgen@PPK v{__version__}) - Character pool config (e.g. upper) must be given as booleans.")

    # 2 - INITIALISE CHARACTERS VARIABLE
    characters = ""

    # 3 - APPEND TO POOL
    if upper: characters += string.ascii_uppercase
    if lower: characters += string.ascii_lowercase
    if numbers: characters += string.digits
    if symbols: characters += string.punctuation

    # 4 - RETURN POOL
    return characters

def generate(upper=True, lower=True, numbers=True, symbols=True, length=10, returnPool=False):
    # 1 - DATA TYPE VALIDATION
    if not(isinstance(length, int)): raise TypeError(f"[202] (passgen@PPK v{__version__}) - Password length must be given as an integer.")
    # 2 - BUILD CHARACTER POOL
    characters = buildPool(upper, lower, numbers, symbols)
    selected = sum([upper, lower, numbers, symbols])
    
    # 3 - VALIDATE LENGTH AND SELECTED CATEGORIES
    if length < selected: raise ValueError(f"[203] (passgen@PPK v{__version__}) - Length must be greater than or equal to the number of character types selected ({selected}).")
    if selected == 0: raise ValueError(f"[204] (passgen@PPK v{__version__}) - You must select at least one type of character.")

    # 4 - INITIALISE CHARSLIST
    charslist = []

    # 5 - GUARANTEE EACH CHARACTER TYPE APPEARS IN THE PASSWORD
    if upper: charslist.append(secrets.choice(string.ascii_uppercase))
    if lower: charslist.append(secrets.choice(string.ascii_lowercase))
    if numbers: charslist.append(secrets.choice(string.digits))
    if symbols: charslist.append(secrets.choice(string.punctuation))

    # 6 - CHOOSE EACH CHARACTER
    while len(charslist) < length:
        # use secrets module to choose from character pool
        charslist.append(secrets.choice(characters))

    # 7 - SHUFFLE PASSWORD SO REQUIRED CHARS AREN'T ALWAYS AT BEGINNING (i.e. Aa1@)
    secrets.SystemRandom().shuffle(charslist)
    password = "".join(charslist)

    # 8 - RETURN PASSWORD (AND POOL if returnPool)
    if returnPool: return password, characters
    return password

def entropy(pool="", length=0):
    # 1 - DATA TYPE VALIDATION
    if not(isinstance(length, int)):
        raise TypeError(f"[206] (passgen@PPK v{__version__}) - Password length must be given as an integer.")
    if not(isinstance(pool, str)):
        raise TypeError(f"[209] (passgen@PPK v{__version__}) - Character pool must be given as a string.")

    # 2 - CHECK POOL HAS BEEN PASSED
    if not pool:
        raise ValueError(f"[207] (passgen@PPK v{__version__}) - Your character pool cannot be empty.")
    
    # 3 - HANDLED NEGATIVE LENGTHS (0.7.1)
    if length < 0:
        raise ValueError(f"[208] (passgen@PPK v{__version__}) - Length must not be a negative number.")

    # 4 - EXCLUDE DUPLICATE CHARS TO ENSURE ENTROPY IS ACCURATE
    poolsize = len(set(pool))

    # 5 - CALCULATE ENTROPY
    entropy = length * math.log2(poolsize)

    # 6 - RETURN ENTROPY
    return entropy