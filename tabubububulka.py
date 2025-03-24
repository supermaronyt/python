def vytiskni_ascii_tabulku(start, konec, sloupce):
    pocet_radku = (konec - start + 1 + sloupce - 1) // sloupce

    horni_hranice = "┌" + "─" * (sloupce * 9 - 1) + "┐"
    print(horni_hranice)
    if sloupce == range(0, 10000):
        if sloupce == 2:
            print("│  ascii tabuůla  │")
        elif sloupce == 3:
            print("│       ascii tabuůla      │")
        elif sloupce == 4:
            print("│            ascii tabuůla          │")
        elif sloupce == 5:
            print("│                 ascii tabuůla              │")

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
