import secrets, string, math

version = "0.7.0"
__all__ = ["generate", "buildPool", "entropy"]

def buildPool(upper=True, lower=True, numbers=True, symbols=True):
    if not(isinstance(upper, bool)) or not(isinstance(lower, bool)) or not(isinstance(numbers, bool)) or not(isinstance(symbols, bool)):
        raise TypeError(f"[201] (passgen@PPK v{version}) - Character pool config (e.g. upper) must be given as booleans.")
    characters = ""
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    return characters

def generate(upper=True, lower=True, numbers=True, symbols=True, length=10, returnPool=False):
    # check data types
    if not(isinstance(length, int)):
        raise TypeError(f"[202] (passgen@PPK v{version}) - Password length must be given as an integer.")
    # generate char pool
    characters = buildPool(upper, lower, numbers, symbols)
    selected = sum([upper, lower, numbers, symbols])
    
    # check pass length and categories
    if length < selected:
        raise ValueError(f"[203] (passgen@PPK v{version}) - Length must be greater than or equal to the number of character types selected ({selected}).")
    if selected == 0:
        raise ValueError(f"[204] (passgen@PPK v{version}) - You must select at least one type of character.")
    
    charslist = []
    # ensure that there is at least one of the characters from each category chosen
    if upper: charslist.append(secrets.choice(string.ascii_uppercase))
    if lower: charslist.append(secrets.choice(string.ascii_lowercase))
    if numbers: charslist.append(secrets.choice(string.digits))
    if symbols: charslist.append(secrets.choice(string.punctuation))

    # choose each character
    while len(charslist) < length:
        # use secrets module to choose from character pool
        charslist.append(secrets.choice(characters))
    
    secrets.SystemRandom().shuffle(charslist)
    password = "".join(charslist)

    # return pool if requested, return password in all cases
    if returnPool: return password, characters
    return password

def entropy(pool="", length=0):
    if not(isinstance(length, int)):
        raise TypeError(f"[206] (passgen@PPK v{version}) - Password length must be given as an integer.")
    
    if not pool:
        raise ValueError(f"[207] (passgen@PPK v{version}) - Your character pool cannot be empty.")
    
    # build pool
    poolsize = len(set(pool))
    entropy = length * math.log2(poolsize)
    return entropy