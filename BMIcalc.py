import math


def bmi():
    print("BMI Calculator")
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    height = height / 100
    Bmi = weight / (height * height)
    Bmi = round(Bmi, 2)
    print("Your BMI is", Bmi)
    if Bmi < 18.5:
        print("You are underweight")
    if 18.5 < Bmi < 25:
        print("You are normal")
    if 25 < Bmi < 30:
        print("You are overweight")
    if 30 < Bmi < 35:
        print("You are obsese")
    if input("do you want to continue?: y/n") == "y":
        Bmi()
    else:
        print("Thank you")
        quit()


bmi()
