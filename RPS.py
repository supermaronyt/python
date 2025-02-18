import random


def rock_paper_scissors():
    print("Welcome to the game of rock paper scissors")
    print("You have to choose rock, paper or scissors")
    choice = input("Enter rock, paper or scissors: ")
    choice_ai = random.choice(["rock", "paper", "scissors"])
    print("AI chose: " + choice_ai)
    match choice:
        case "rock":
            if choice_ai == "rock":
                print("DRAW!")
            elif choice_ai == "paper":
                print("You lose")
            elif choice_ai == "scissors":
                print("You win")

        case "paper":
            if choice_ai == "rock":
                print("You win")
            elif choice_ai == "paper":
                print("DRAW")
            elif choice_ai == "scissors":
                print("You lose")

        case "scissors":
            if choice_ai == "rock":
                print("You lose")
            elif choice_ai == "paper":
                print("You win")
            elif choice_ai == "scissors":
                print("DRAW")

        case _:
            print("Invalid input")

    if input("do you wanna play again? (y/n): ") == "y":
        rock_paper_scissors()
    else:
        quit()


rock_paper_scissors()
