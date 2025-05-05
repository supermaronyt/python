
pocet_aut = int(input("Zadejte počet aut: "))
auta = []


for i in range(pocet_aut):
    auto = input(f"Zadejte název auta {i + 1}: ")
    auta.append(auto)


print("Názvy aut:", ", ".join(auta))


pocet_parametru = int(input("Zadejte počet parametrů: "))
parametry = []


for i in range(pocet_parametru):
    parametr = input(f"Zadejte název parametru {i + 1}: ")
    parametry.append(parametr)

print("Názvy parametrů:")
for parametr in parametry:
    print(parametr)


tabulka = []
for auto in auta:
    radek = []
    for parametr in parametry:
        hodnota = input(f"Zadejte hodnotu parametru '{parametr}' pro auto '{auto}': ")
        radek.append(hodnota)
    tabulka.append(radek)


print("\nTabulka aut a parametrů:")
print(f"{'Auto':<15}", end="")
for parametr in parametry:
    print(f"{parametr:<15}", end="")
print()

for i, auto in enumerate(auta):
    print(f"{auto:<15}", end="")
    for hodnota in tabulka[i]:
        print(f"{hodnota:<15}", end="")
    print()
