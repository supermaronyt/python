x = int(input("Enter a number for facturation: "))
result = 1
factors = []
for i in range(1,x+1):
    result = result * i
    factors.append(str(i))
    print("factorial of number " + str(i) + " is " + str(result) + " and its the result of multiplying: " )
    print(factors)
