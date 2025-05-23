import builtins
from builtins import print, len, range, chr, int, input, str


def vytiskni_ascii_tabulku(start, konec, sloupce):
    pocet_radku = (konec - start + 1 + sloupce - 1) // sloupce

    horni_hranice = "┌" + "─" * (sloupce * 9 - 1) + "┐"
    print(horni_hranice)

    celkova_sirka = sloupce * 9 - 2
    text = "ascii tabulka"
    mezery = (celkova_sirka - len(text)) // 2
    extra_mezera = (celkova_sirka - len(text)) % 2
    print("│" + " " * mezery + text + " " * (mezery + extra_mezera) + " │")

    for radek in range(pocet_radku):
        prostredni_hranice = "├" + "─" * (sloupce * 9 - 1) + "┤"
        print(prostredni_hranice)
        for sloupec in range(sloupce):
            index = start + radek + sloupec * pocet_radku
            if index <= konec:
                print("│ " + str(index).rjust(3) + ": " + chr(index) + " ", end="")
            else:
                print("│        ", end="")
        print("│")

    dolni_hranice = "└" + "─" * (sloupce * 9 - 1) + "┘"
    print(dolni_hranice)

start = int(input("Zadej počáteční ASCII hodnotu: "))
konec = int(input("Zadej koncovou ASCII hodnotu: "))
sloupce = int(input("Zadej počet sloupců: "))

vytiskni_ascii_tabulku(start, konec, sloupce)
