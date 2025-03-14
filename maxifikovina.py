schranky = []
x = input("zadejte pocet schranek: ")
x = int(x)

while x > 0:
    y = input("zadejte obsah schranky: ")
    schranky.append(int(y))
    x -= 1

pozadovana_hodnota = int(input("zadejte pozadovanou hodnotu: "))
celek = 0


for s1 in schranky:
    for s2 in schranky:
        if s1 + s2 == pozadovana_hodnota:
            celek = pozadovana_hodnota
            print("Našli jsme dvojici:  a = ", s1, "b = ", s2)
            break
    if celek == pozadovana_hodnota:
        break

if celek == pozadovana_hodnota:
    print("Součet je roven požadované hodnotě.")
else:
    print("Taková dvojice neexistuje.")

