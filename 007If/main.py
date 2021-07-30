def approved(_n):
    n=int(_n)
    if n>=5:
        return "You pass the examen"
    else:
        return "You have to repeat another year"

note=input("What's your note? ")
print(approved(note))