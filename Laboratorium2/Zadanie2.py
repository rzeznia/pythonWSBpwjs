# Utwórz program, który wczytuje komunikat użytkownika, a następnie wypisuje go
# w odwrotnej kolejności.

#string=input("Podaj tekst do odwrócenia")
def reverse(string):
    length = len(string)
    str2 = ''
    for x in range(0, length).__reversed__():
        str2 = str2+string[x]
    return str2

print(reverse(string=input("Podaj tekst do odwrócenia")))

