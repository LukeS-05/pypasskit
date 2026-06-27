import secrets, string, math

version = "1.0.0-b3"

__all__ = ["password", "passphrase"]

def generatePool(upperletters=True, lowerletters=True, numbers=True, symbols=True):
    characters = ""
    if upperletters:
        characters += string.ascii_uppercase
    if lowerletters:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    return characters

def generatePassword(upperletters=True, lowerletters=True, numbers=True, symbols=True, length=10, entropy=False):
    # check data types
    if not(isinstance(upperletters, bool)) or not(isinstance(lowerletters, bool)) or not(isinstance(numbers, bool)) or not(isinstance(symbols, bool)):
        raise TypeError(f"Error 201 (passgenapi v{version}) - Configuration flags must be booleans.")
    if not(isinstance(length, int)):
        raise TypeError(f"Error 202 (passgenapi v{version}) - Password length must be an integer.")
    # generate char pool
    characters = generatePool(upperletters, lowerletters, numbers, symbols)
    selected = sum([upperletters, lowerletters, numbers, symbols])
    
    # check pass length and categories
    if length < selected:
        raise ValueError(f"Error 203 (passgenapi v{version}) - Requested password length must accomodate at least one of each selected character category.")
    if selected == 0:
        raise ValueError(f"Error 204 (passgenapi v{version}) - No character types selected. You must enable at least one pool category.")
    
    charslist = []
    # ensure that there is at least one of the characters from each category chosen
    if upperletters: charslist.append(secrets.choice(string.ascii_uppercase))
    if lowerletters: charslist.append(secrets.choice(string.ascii_lowercase))
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
    if entropy==True:
        entropy = length * math.log2(len(characters))
        return password, entropy
    else:
        return password
    
def generatePassphrase(file, number=4, delimiter="-"):
    # open file and read the word on each line
    with open(file, "r") as f:
        words = f.read().splitlines()
    
    # remove blank lines
    if "" in words:
        words.remove("")
    
    passphrase = ""
    for i in range(number):
        chosen = secrets.choice(words)
        
        passphrase += chosen
        # to prevent delimiter at the end
        if i != (number-1):
            passphrase += delimiter
        
    return passphrase