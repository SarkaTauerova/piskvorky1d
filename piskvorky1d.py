#piskvorky1d.py
from random import randrange

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"    
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah(pole, pozice, symbol):
    if (pozice < 0) or (pozice >= (len(pole))):
        raise ValueError("Můžeš hrát pouze na pozice od 0 do 19")
    elif ((symbol != 'x') and (symbol != 'o')):
        raise ValueError("To není platný symbol")
    elif (pole[pozice] != ('-')):
        raise ValueError("Tam nejde hrát, vyber si neobsazenou pozici")
    else:
        zacatek = pole[:pozice]
        konec = pole[pozice + 1:]
        pole = zacatek + symbol + konec
        return pole

def tah_hrace(pole, symbol):
    while True:
        odpoved = input('Na jakou pozici chceš hrát?: ')
        try:
            pozice = int(odpoved)
        except ValueError:
            print('Zadávej čísla!')
        else:
            try:
                nove_pole = tah(pole, pozice, symbol)
            except ValueError:
                print("Tam nejde hrát")
            else:
                return nove_pole          

def tah_PC(pole, symbol):
    while True:
        pozice = randrange(len(pole))
        if pole[pozice] == "-":
            nove_pole = tah(pole, pozice, symbol)
            return nove_pole

def piskvorky1d():
    pole = "-" * 20
    while True:
        pole = tah_hrace(pole, "o")
        print("Tvůj tah je: " + (pole))
        if vyhodnot(pole) != "-":
            break
        pole = tah_PC(pole, "x")
        if vyhodnot(pole) != "-":
            break
        print("Tah počítače je: " + (pole))
    if vyhodnot(pole) == "!":
        print("Remíza")
    elif vyhodnot(pole) == "o":
        print("Vyhrál jsi")
    elif vyhodnot(pole) == "x":
        print("Vyhrál počítač")

piskvorky1d()
