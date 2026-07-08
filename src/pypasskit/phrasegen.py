import secrets, math
from importlib.metadata import version

__version__ = version("pypasskit") 
__all__ = ["generate","entropy"]

def generate(file=None, wordlist=None, length=4, delimiter="-"):
    # open file and read the word on each line
    if file and wordlist: raise ValueError(f"[212] (phrasegen@PPK v{__version__} - You must pass EITHER file or wordlist as argument\nBoth have been passed.")
    if not file and not wordlist: raise ValueError(f"[213] (phrasegen@PPK v{__version__} - You must pass EITHER file or wordlist as argument\nNeither has been passed.")
    if file:
        try:
            with open(file, "r") as f:
                words = f.read().splitlines()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"[211] (phrasegen@PPK v{__version__}) - File does not exist. - {e}")
    elif wordlist:
        if not(isinstance(wordlist, list)):
            raise ValueError(f"[214] (phrasegen@PPK v{__version__} - Wordlist must be a lists")
        words = wordlist
    # remove blank lines
    words = [w for w in words if w.strip()]
    
    passphrase = ""
    for i in range(length):
        chosen = secrets.choice(words)
        
        passphrase += chosen
        # to prevent delimiter at the end
        if i != (length-1):
            passphrase += delimiter
        
    return passphrase

def entropy(file=None, wordlist=None, length=0):
    # open file and read the word on each line
    if file and wordlist: raise ValueError(f"[212] (phrasegen@PPK v{__version__} - You must pass EITHER file or wordlist as argument\nBoth have been passed.")
    if not file and not wordlist: raise ValueError(f"[213] (phrasegen@PPK v{__version__} - You must pass EITHER file or wordlist as argument\nNeither has been passed.")
    if file:
        try:
            with open(file, "r") as f:
                words = f.read().splitlines()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"[211] (phrasegen@PPK v{__version__}) - File does not exist. - {e}")
    elif wordlist:
        if not(isinstance(wordlist, list)):
            raise ValueError(f"[214] (phrasegen@PPK v{__version__} - Wordlist must be a lists")
        words = wordlist
    # remove blank lines
    words = [w for w in words if w.strip()]
        
    entropy = length * math.log2(len(words))
    return entropy