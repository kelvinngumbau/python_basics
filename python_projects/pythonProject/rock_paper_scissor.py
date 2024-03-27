import random

user_score = 0
computer_score = 0
options = ["rock","paper","scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit ").lower()

    if user_input == "q":

        break

    if user_input not in options:

        continue

    random_number = random.randint(0,2)

    computer_pick = options[random_number]

    print("computer picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":

        print("you won")

        user_score += 1

    elif user_input == "paper" and computer_pick == "rock":

        print("you won")
        user_score += 1
    elif user_input == "scissors" and computer_pick == "paper":

        print("you won")
        user_score += 1

    else:

        print("computer won")

        computer_score += 1

print("you scored",user_score,".")
print("computer scored",computer_score,".")
print("goodbye, see you next time")
