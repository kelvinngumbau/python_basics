print("You are welcome to play this game and I hope you will enjoy it")
print("Your answers should be in lowercase")
ans = input("Are you ready to start the game (yes/no) ")

if ans.lower() != "yes":
    quit()

answer = input("What it is your favourite fruit? (mangoes/banana) ").lower()

if answer == "mangoes":

    answer = input("select left or right (right/left)").lower()

    if answer == "left":

        print("Oops there is a river in this side")

        river = input("Do you know how to swim? (yes/no) ").lower()

        if river == "yes":

            crocodile =input("Also take note that there are crocodile in this river, would you wish to proceed (yes/no)" ).lower()

            if crocodile == "yes":

                swim = input("can you swim? (yes/no) ").lower()

                if swim == "yes":

                    print("Enjoy mangoes to your satisfication")

    elif answer == "right":

        land = input("Do you love pineapple? (yes/no) ").lower()

        if land == "yes":


            climb = input("can you climb a mountain (yes/no) ").lower()

            if climb == "yes":

                print("take this road and you will enjoy pineapple")
        
else:

    if answer == "banana":

        answ = input("Glad you like banana. Can climb a tree? (yes/no) ").lower()

        if answ == "yes":

            walk = input("how long ca you walk? (5 km/ 10 km)").lower()

            if walk == "10 km":

                panga = input("Do you knoe how to use a panga or knife? (panga/knife)").lower()

                if panga == "panga":

                    print("Enjoy bananas to your satisfication")
