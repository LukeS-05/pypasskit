import math
import pypasskit as ppk

def main(): 
    # MAIN CODE
    print(r""" ____  ____  _  __   PYPASSKIT DEMO
|  _ \|  _ \| |/ /   To learn more about this demo, go to
| |_) | |_) | ' /    https://lukes-05.github.io/pypasskit/docs
|  __/|  __/| . \     
|_|   |_|   |_|\_\   Copyright (C) 2026 LukeS-05 - MIT License.
______________________________________________________________________________________
    """)

    # SETTINGS
    try:
        length = int(input("Number of words: "))
    except ValueError:
        length = 4
        print("Length = 4")

    delimiter = input("Delimiter (e.g. -): ")

    print("-"*90)

    # ------------------------------------ THIS IS WHERE PYPASSKIT IS USED!!!
    # GENERATE PASSWORD
    generated = ppk.phrasegen.generate(length=length, delimiter=delimiter)
    entropy = ppk.phrasegen.entropy(length=length)
    # -----------------------------------

    # PRINT PASSWORD AND ENTROPY
    print(f"Passphrase - {generated}")
    print(f"Entropy - {math.floor(entropy)} bits")
    input("Press ENTER to continue")

if __name__ == "__main__":
    main()