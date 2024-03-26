import random

guess = input("Enter a number please ")


if guess.isdigit():

    guess = int(guess)

    if guess <= 0:

        print("Please enter a number greater than zero")

        quit()

else:

    print("Please enter a number next time")

    quit()

random_number = random.randint(0,guess)

print(random_number)

guesses = 0

while True:
    guesses += 1
    guess_number = input("Make a Guess ")

    if guess_number.isdigit():

        guess_number = int(guess_number)

    else:

        print("Please enter a number next time")

        continue

    if guess_number == random_number:

        print("correct")

        break

    else:

        if guess_number > random_number:

            print("Too high")

        else:

            print("Too low")

print("you got it in ",guesses,"guesses")
print("congratulation for your efforts")













