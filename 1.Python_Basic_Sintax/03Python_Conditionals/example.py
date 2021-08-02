#Hit the number
import random
number=random.randint(0,100)
finish=False

while(finish==False):
    usernumber=input("What number i'm thinking now?? ")
    usernumber=int(usernumber)

    if usernumber==number:
        print("Yes!! Congratulations my friend!")
        finish=True
    elif usernumber<number:
        print("No, its bigger")
    else:
        print("No, its smaller")