# Napisz program, który podany przez użytkownika ciąg znaków szyfruje przy
# użyciu szyfru Cezara i wyświetla zaszyfrowany tekst.

string = input("Podaj string do zaszycezarowania ")
string2 = ''
for letter in string:
    string2 += chr(ord(letter) + 3)
print("Zaszycezarowane: " + string2)   #to rozwiazanie jest SŁABE!
# TODO: ZROBIC TO LEPIEJ