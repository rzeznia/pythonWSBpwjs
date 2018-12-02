a = int(input("Podaj bok a"))
b = int(input("Podaj bok b"))
c = int(input("Podaj bok c"))

if a < b+c  and b < a+c  and c < a+b :
    print("Można zbudowac trojakt")
else:
    print("Nie mozna zbudowac trojkata")
