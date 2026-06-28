import secrets, math

version = "0.6.1"
__all__ = ["generate","entropy"]

def generate(file, number=4, delimiter="-"):
    # open file and read the word on each line
    with open(file, "r") as f:
        words = f.read().splitlines()
    
    # remove blank lines
    words = [w for w in words if w.strip()]
    
    passphrase = ""
    for i in range(number):
        chosen = secrets.choice(words)
        
        passphrase += chosen
        # to prevent delimiter at the end
        if i != (number-1):
            passphrase += delimiter
        
    return passphrase

def entropy(file, chosen=0):
    with open(file, "r") as f:
        words = f.read().splitlines()
    
    # remove blank lines
    words = [w for w in words if w.strip()]
        
    entropy = chosen * math.log2(len(words))
    words = ""
    return entropy