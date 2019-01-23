print('To samo co Laboratorium 2 -> Zadanie 3')
print('')

# Popraw program Wymieszane litery tak, żeby każdemu słowu towarzyszyła
# podpowiedź. Gracz powinien mieć możliwość zobaczenia podpowiedzi, jeśli
# utknie w martwym punkcie. Dodaj system punktacji, który nagradza graczy
# rozwiązujących anagram bez uciekania się do podpowiedzi
#
# .
import random
slowa = ("python","gdansk","dlaczego","gdynia","wsb")
hints = ("Język programowania", "Miasto w Polsce", "Cos co mówimy gdy nie rozumiemy jak coś działa", "Miasto w Polsce", "Uczelnia prywatna")
word = random.choice(slowa)
hint = ''
c = 0
for slowo in slowa:
    if slowo == word:
        hint = hints[c]
    else:
        c += 1
#print (word)
poprawnie = word
pomie =""
while word:
    position = random.randrange(len(word))
    pomie += word[position]
    word = word[:position] + word[(position + 1):]
print (pomie)
print(
"""
Witaj w grze 'Wymieszane litery'!
Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez
podawania odpowiedzi.)
""")
tries = 0
print("Zgadnij, jakie to słowo:", pomie)
zgaduj = input("\nTwoja odpowiedź: ")
while zgaduj != poprawnie and zgaduj != "":
    print("Niestety, to nie to słowo.")
    zgaduj = input("Twoja odpowiedź: ")
    tries += 1
    if(tries >= 2):
        print("Podpowiedź: " + hint)
if zgaduj == poprawnie:
    print("Zgadza się! Zgadłeś!\n")
print("Dziękuję za udział w grze.")