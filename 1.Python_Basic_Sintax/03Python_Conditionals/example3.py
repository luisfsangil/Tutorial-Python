#Using 'if', and 'else' combined with 'and', 'or', 'not'

print("In this club only enter girls that have 21 years or more")
print("If you are a boy or if you don't have 21 yet, you have to pay 50 dolars\n")

sex=bool(input("Are you a girl (say True or False please)? "))
if sex:
    age=int(input("What's your age? "))
if not(sex and age>21):
    payed=bool(input("You Want to pay 50 dolars (say True or False please)? "))

if (sex and age>=21) or payed:
    print("Welcome to our club! ")
else:
    print("Sorry, you can't enter here")