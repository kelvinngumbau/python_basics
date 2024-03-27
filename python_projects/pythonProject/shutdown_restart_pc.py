import os


while True:

    user_input = input("Do you want to restart or shutdown? (restart/shutdown) ").lower()

    if user_input == "restart":

        restart_pc = input("You are about to restart your pc? (yes/no)")

        if restart_pc == "yes":

            os.system("shutdown /r/t 30")
        else:

            break
    else:

        shutdown_pc = input("You are about to shutdown your (yes/no) ").lower()

        if shutdown_pc == "yes":

            os.system("shutdown /s")

        else:

            break


print("Python is awesome for automation")