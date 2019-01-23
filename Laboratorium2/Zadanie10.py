# Pobierz od użytkownika n liczb i zapisz je w liście. Wydrukuj:  
# 1. elementy listy i ich indeksy,  
# 2. elementy w odwrotnej kolejności,  
# 3. posortowane elementy.  
# 4. Usuń z listy pierwsze wystąpienie elementu podanego przez użytkownika.  
# 5. Usuń z listy element o podanym indeksie.  
# 6. Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu.  
# 7. Wybierz z listy elementy od indeksu i do j

lista = []
cd = []
n = input('podaj n liczb do dodania')
for x in range(int(n)):
    liczba = input('Podaj liczbę nr ' + str(x+1) +': ')
    lista.append(int(liczba))
    cd.append(int(liczba))

print('1. ELementy listy:')
for x in range(int(n)):
    print("Indeks: " + str(x+1) + ' = ' + str(lista[x]) )

print('2. Odwrotne:')
cd.reverse()
print(cd)
cd.reverse()

print('3. Sort:')
cd.sort()
print(cd)

print('4. Usuń z listy pierwsze wystąpienie elementu podanego przez użytkownika.')
usidx = input("Podaj element któy chcesz usunąć: ")
delval = int(usidx)
try:
    lista.remove(delval)
    print(lista)
except ValueError:
    print('Nie ma takiego elementu w liście')

print('5. Usuń z listy element o podanym indeksie.')
usidx = input("Podaj indeks któy chcesz usunąć: ")
idx = int(usidx)
try:
    val = lista.pop(idx)
    print('Usunięto index '+usidx + ' o wartosci: '+ str(val))
    print(lista)
except IndexError:
    print('Brak w liście elementu o podanym indeksie')

print('6. Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu.')
usidx = input("Podaj element którego szukasz: ")
idx = int(usidx)
try:
    cnt = lista.count(idx)
    fidx = lista.index(idx)
    print('Element w liście pojawia się razy: '+ str(cnt))
    print('Pierwszy index znalezionego elementu to: ' + str(fidx))
except ValueError:
    print('Nie ma takiego elementu w liscie')

print('7. Wybierz z listy elementy od indeksu i do j')
start = input('Podaj wartość startową (i)')
stop = input('Podaj wartość startową (j)')
print(lista)
for x in range(int(start), int(stop)+1):
    print(lista[x])