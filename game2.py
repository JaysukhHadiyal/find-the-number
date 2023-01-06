import random
random_no = random.randint(1, 100)
try:
    print("you enter number 1 to 100")
    guess1 = None               # enter you chose total guess
    guess1 = int(input("enter you chose guess"))
    print(f"you total guess is :{guess1}")
    guess = 0                   # you total guess
    guess2 = 1                  # how to guess you`r done
    user = None
    num = 0

    while (random_no != user):
        num += 1
        user = int(input(f"NO.{num} enter the number:"))
        print(f"your guess number is done :{guess2}")

        guess += 1

        guess2 += 1
        if (user == random_no):
            print("you guess write")
        elif (user >= 101):
            print("you cross the limit, you enter only 1,100")
            break
        else:
            if (random_no >= user):
                print("you guess wrong enter the larger number ")
            else:
                print("you guess wrong enter the smaller number")

        if (guess >= guess1):
            print("you cross the limit ")
            break
    print(f"the total guess is : {guess}")
    print(f"your write guess is : {random_no}")
except ValueError:
    print("you enter invalid key")