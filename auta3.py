# -*- coding: utf-8 -*-
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from tabulate import tabulate
except ImportError:
    install("tabulate")
    from tabulate import tabulate

try:
    from colorama import Fore, Style, init
except ImportError:
    install("colorama")
    from colorama import Fore, Style, init

init(autoreset=True)

from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

pocet_aut = int(input("Zadejte pocet aut: "))
auta = []

for i in range(pocet_aut):
    auto = input(f"Zadejte nazev auta {i + 1}: ")
    auta.append(auto)

print(Fore.CYAN + "Nazvy aut:", ", ".join(auta))

pocet_parametru = int(input("Zadejte pocet parametru (minimalne 2): "))
parametry = ["cena", "procenta"]

for i in range(2, pocet_parametru):
    parametr = input(f"Zadejte nazev parametru {i + 1}: ")
    parametry.append(parametr)

print(Fore.CYAN + "Nazvy parametru:")
for parametr in parametry:
    print(Fore.YELLOW + parametr)

tabulka = []
for auto in auta:
    radek = []
    for parametr in parametry:
        hodnota = input(f"Zadejte hodnotu parametru '{parametr}' pro auto '{auto}': ")
        radek.append(float(hodnota) if parametr in ["cena", "procenta"] else hodnota)
    tabulka.append(radek)

pocet_let = int(input("Zadejte pocet let pro hodnoceni: "))

print(Fore.GREEN + "\nTabulka nakladu na vlastnictvi:")
hlavicka = ["Rok"] + auta
data = []

for rok in range(1, pocet_let + 1):
    radek = [rok]
    for i, auto in enumerate(auta):
        cena = tabulka[i][0]
        procenta = tabulka[i][1]
        snizena_cena = cena * ((1 - procenta / 100) ** (rok - 1))
        radek.append(f"{snizena_cena:.2f}")
    data.append(radek)

print(tabulate(data, headers=hlavicka, tablefmt="fancy_grid"))

print(Fore.GREEN + "\nTabulka snizeni hodnoty aut:")
hlavicka_snizeni = ["Rok"] + auta
data_snizeni = []

for rok in range(1, pocet_let + 1):
    radek = [rok]
    for i, auto in enumerate(auta):
        cena = tabulka[i][0]
        procenta = tabulka[i][1]
        hodnota_aktualni = cena * ((1 - procenta / 100) ** (rok - 1))
        hodnota_predchozi = cena * ((1 - procenta / 100) ** (rok - 2)) if rok > 1 else cena
        snizeni = hodnota_predchozi - hodnota_aktualni
        radek.append(f"{snizeni:.2f}")
    data_snizeni.append(radek)

print(tabulate(data_snizeni, headers=hlavicka_snizeni, tablefmt="fancy_grid"))

print(Fore.GREEN + "\nZbytek parametru:")
for i, auto in enumerate(auta):
    print(Fore.MAGENTA + f"\n{auto}:")
    for j in range(2, len(parametry)):
        print(Fore.YELLOW + f"{parametry[j]}: {tabulka[i][j]}")

print(Fore.GREEN + "\nTabulka kumulovanych nakladu na vlastnictvi:")
hlavicka_kumulovane = ["Rok"] + auta
data_kumulovane = []

for rok in range(1, pocet_let + 1):
    radek = [rok]
    for i, auto in enumerate(auta):
        cena = tabulka[i][0]
        procenta = tabulka[i][1]
        provozni_naklady = sum(
            float(tabulka[i][j]) for j in range(2, len(parametry))
        )
        if rok == 1:
            kumulovane_naklady = cena + provozni_naklady
        else:
            hodnota_predchozi = cena * ((1 - procenta / 100) ** (rok - 2))
            hodnota_aktualni = cena * ((1 - procenta / 100) ** (rok - 1))
            ztrata_hodnoty = hodnota_predchozi - hodnota_aktualni
            kumulovane_naklady += provozni_naklady + ztrata_hodnoty
        radek.append(f"{kumulovane_naklady:.2f}")
    data_kumulovane.append(radek)

print(tabulate(data_kumulovane, headers=hlavicka_kumulovane, tablefmt="fancy_grid"))
