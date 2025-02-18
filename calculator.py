def main():
    try:
        x = int(input("Zadejte číslo: "))
        y = int(input("Zadejte druhé číslo: "))
        z = input("Zadejte operátor: ")



        match z:
            case "+":
                print(x + y)
            case "-":
                print(x - y)
            case "*":
                print(x * y)
            case "/":
                print(x / y)
    except:
        print("chybička se vbloudila")
        main()
