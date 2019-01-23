print('To samo co Laboratorium 2 -> Zadanie 3')
print('')


import random
slowa = ("python","gdansk","dlaczego","gdynia","wsb")

asks = 0
letters = []
print('''Siemaszko, wybrałem dla Ciebie słowo do odgadnięcia. 
Możesz zadać mi 5 pytań czy literka którą wybrałeś znajduje sie w słowie.''')
word = random.choice(slowa)
print("Wybrane słowo ma " + str(len(word)) + "liter")
print(word)
while asks < 5:
    if asks > len(word):
        break
    print("\nPozostało Ci " + str(int(5-asks)) + "pytań")
    print("Zadaj pytanie o literę")
    letter = input("Litera")   #brak sprawdzania czy to litera czy string, wiem :(
    if letter in word:
        print("Litera jest w słowie!")
        letters.append(letter)
    else:
        print("Litery nie ma w słowie")
    asks +=1
print("Twoje trafione litery to:")
print(letters)
for x in range(1, len(word)):
    print("__ ", end='')
zgaduj = input("\n Zgadnij słowo:")
while zgaduj != word and zgaduj != "":
    print("Niestety, to nie to słowo.")
    zgaduj = input("\n Zgadnij słowo:")
if zgaduj == word:
    print("Zgadza się! Zgadłeś!\n")
print("Dziękuję za udział w grze.")