import secrets, string, math

version = "0.6.0"
__all__ = ["generate", "buildPool", "entropy"]

def buildPool(upper=True, lower=True, numbers=True, symbols=True):
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

def generate(upper=True, lower=True, numbers=True, symbols=True, length=10):
    # check data types
    if not(isinstance(upper, bool)) or not(isinstance(lower, bool)) or not(isinstance(numbers, bool)) or not(isinstance(symbols, bool)):
        raise TypeError(f"Error 201 (pypasskit v{version}) - Configuration flags must be booleans.")
    if not(isinstance(length, int)):
        raise TypeError(f"Error 202 (pypasskit v{version}) - Password length must be an integer.")
    # generate char pool
    characters = buildPool(upper, lower, numbers, symbols)
    selected = sum([upper, lower, numbers, symbols])
    
    # check pass length and categories
    if length < selected:
        raise ValueError(f"Error 203 (pypasskit v{version}) - Requested password length must accomodate at least one of each selected character category.")
    if selected == 0:
        raise ValueError(f"Error 204 (pypasskit v{version}) - No character types selected. You must enable at least one pool category.")
    
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
    charslist = []
    # password entropy check
    return password
    
def entropy(pool="", length=0):
    entropy = length * math.log2(len(pool))
    return entropy