def whilefunc(number):
    x = int(input("Enter a number of numbers you want to sum: "))

    while x > 0:
        number += int(input("Enter a number: "))
        x -= 1
    print(number)
def forfunc(number):
    for i in range(0, int(input("zadejte cislo: "))):
        number += int(input("Enter a number: "))
        print(number)


number = 0
if input("choose function: forfunc, whilefunc   ") == "forfunc":
    forfunc(number)
else:
    whilefunc(number)
