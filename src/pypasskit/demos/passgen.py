import math
import pypasskit as ppk

# USED FOR CONVERTING Y/N (YES/NO) TO BOOLEAN.
def updateConfig(text):
    while True:
        var = input(f"{text} (yes / no): ").lower().strip()
        if var == "": continue # if no input
        elif var[0] == "y": return True # if yes
        elif var[0] == "n": return False # if no

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
    upperletters = updateConfig("Uppercase letters? ")
    lowerletters = updateConfig("Lowercase letters? ")
    numbers = updateConfig("Numbers? ")
    symbols = updateConfig("Symbols? ")

    try:
        length = int(input("Length of password: "))
    except ValueError:
        length = 12
        print("Length = 12")

    print("-"*90)

    # ------------------------------------ THIS IS WHERE PYPASSKIT IS USED!!!
    # GENERATE PASSWORD
    generated, pool = ppk.passgen.generate(upperletters, lowerletters, numbers, symbols, length, True)

    # ENTROPY
    entropy = ppk.passgen.entropy(pool, len(generated))

    # -----------------------------------

    # PRINT PASSWORD AND ENTROPY
    print(f"Password - {generated}")
    print(f"Entropy - {math.floor(entropy)} bits")
    input("Press ENTER to continue")

if __name__ == "__main__":
    main()