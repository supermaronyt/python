numbers = []
def zadavani():
    numbers.append(int(input("zadejte cislo: ")))
    print("soucet cisel je:")
    print(sum(numbers))
    print("pocet cisel je:")
    print(len(numbers))
    if input("Chcete pokracovat? (ano/ne): ") == "ano":
        zadavani()
    else:
        print("Konec zadavani.")
        print("Soucet zadanych cisel je:")
        print(sum(numbers))
        print("Pocet zadanych cisel je:")
        print(len(numbers))
        quit()

zadavani()
