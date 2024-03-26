print("Welcome to python Quiz Game")
print("Only answers in lowercase letters are allowed")
print("Are you ready to play this game ")

score = 0

ans = input("")

if ans.lower() != "yes":

    quit()

else:

    answer = input("ip stands for ")

    if answer.lower() == "internet protocol":

        print("correct")

        score += 1

    else:

        print("wrong")

answer = input("TCP stands for ")

if answer.lower() == "transmission control protocol":

    print("correct")

    score += 1

else:

    print("wrong")


answer = input("Who is the first president of kenya ")

if answer.lower() == "jomo kenyatta":

    print("correct")

    score += 1

else:

    print("wrong")


answer = input("The first president of America ")

if answer.lower() == "george washington":


    print("correct")

    score += 1

else:

    print("wrong")



print("your total score is ", score)
print("Your percentage score is ", (score/4 * 100))