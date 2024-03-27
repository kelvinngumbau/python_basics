mast_pass = input("Enter master password ")

def view():

    with open("account.txt", "r") as f:

        for line in f.readlines():

            x = line.rstrip()

            print(x)

def add():

    name = input("Enter your name ")
    password = input("Enter your password ")

    with open("account.txt", "a") as f:

        f.write(name + "|" + password + "\n")

while True:

    mode = input("What would you like to (view/add or q) ")

    if mode == "q":
        view()
        break

    if mode == "view":

        view()

    elif mode == "add":

        add()