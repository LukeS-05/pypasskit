#  ____  ____  _  __   To learn more about the PyPassKit source code, please go to
# |  _ \|  _ \| |/ /   https://lukes-05.github.io/pypasskit/source
# | |_) | |_) | ' /    
# |  __/|  __/| . \    Copyright (C) 2026 LukeS-05 - This library is licensed under the 
# |_|   |_|   |_|\_\   MIT License 
# ______________________________________________________________________________________

import secrets, math
from importlib.metadata import version
import importlib.resources as resources

__version__ = version("pypasskit") 
__all__ = ["generate","entropy"]

# 0.7.1 - NEW WORDSLIST FUNCTION TO REPLACE IDENTICAL CODE IN TWO FUNCTIONS
def wordsList(file=None, wordlist=None):
    # 1 - GENERATE WORDLIST
    # RULE 1 - IF BOTH ARE PASSED, RAISE VALUEERROR
    if file and wordlist: raise ValueError(f"[212] (phrasegen@PPK v{__version__}) - You must pass EITHER file or wordlist as argument\nBoth have been passed.")
    # RULE 2 - IF NEITHER IS PASSED, USE EFF WORDS LIST
    if not file and not wordlist: 
        try:
            with resources.files("pypasskit").joinpath("eff-words.txt").open("r", encoding="utf-8") as f:
                words = f.read().splitlines()
        except Exception as e:
            raise RuntimeError(f"[219] (phrasegen@PPK v{__version__}) {e}")
    # RULE 3 - IF ONLY FILE IS PASSED, USE FILE
    elif file:
        try:
            # 0.7.1 - FIX FOR UnicodeDecodeError
            with open(file, "r", encoding="utf-8") as f:
                words = f.read().splitlines()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"[211] (phrasegen@PPK v{__version__}) - File does not exist. - {e}")
    # RULE 4 - IF ONLY WORD LIST IS PASSED, USE WORD LIST
    elif wordlist:
        if not(isinstance(wordlist, list)):
            raise ValueError(f"[214] (phrasegen@PPK v{__version__}) - Wordlist must be a lists")
        words = wordlist
    # 2 - REMOVE SPACES FROM WORD LIST
    words = [w for w in words if w.strip()]

    # 3 - RETURN WORDS
    return words

def generate(file=None, wordlist=None, length=4, delimiter="-"):
    # 1 - GENERATE WORDSLIST
    words = wordsList(file, wordlist)
    
    passphrase = "" # nosec 
    for i in range(length):
        chosen = secrets.choice(words)
        
        passphrase += chosen
        # to prevent delimiter at the end
        if i != (length-1):
            passphrase += delimiter
        
    return passphrase

def entropy(file=None, wordlist=None, length=0):
    words = wordsList(file, wordlist)
        
    entropy = length * math.log2(len(set(words))) # 0.7.1 - DON'T ALLOW DUPLICATE WORDS
    return entropy