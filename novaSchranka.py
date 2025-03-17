schranky = []
x = input("zadejte pocet schranek: ")
x = int(x)

while x > 0:
    y = input("zadejte obsah schranky: ")
    schranky.append(int(y))
    x -= 1

pozadovana_hodnota = int(input("zadejte pozadovanou hodnotu: "))
celek = 0
nalezeno = False

for i in range(len(schranky)):
    for j in range(i + 1 , len(schranky)):
        if schranky[i] + schranky[j] == pozadovana_hodnota:
            print("nasli jsme dvojici a=", schranky[i], "b=", schranky[j])
            nalezeno = True
if not nalezeno:
    print("takova kombinace neexistuje")
else:
    print("dalsi nenaleznuto")
