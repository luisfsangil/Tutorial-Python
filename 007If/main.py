def approved(_n):
    n=int(_n)
    if n<5:
        return "You have to repeat another year"
    elif n>=5 and n<7:
        return "You pass the exam"
    elif n>=7 and n<9:
        return "You have a notable"
    elif n>=9 and n<=10:
        return "You have the best note"
    else:
        return "Note incorrect"

    
note=input("What's your note? ")
print(approved(note))