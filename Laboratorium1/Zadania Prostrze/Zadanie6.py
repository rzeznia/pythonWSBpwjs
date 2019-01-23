# Napisz program, który oblicza średnie spalanie samochodu. Wiadomo,
# że trzeba podać dystans który się przejechało i ilość paliwa, którą się
# zużyło. Pamiętajmy, że nasz program powinien być odporny na
# sytuację liczb ujemnych
# Podaj ilość przejechanych kilometrów 600
# Podaj ilość zatankowanych litrów paliwa 36
# Twoja fura spala 6.0 litrów


strkm = input('Podaj ilość przejechanych kilometrów: ')
km = int(strkm)
strlitr = input('Podaj ilość zatankowanych litrów paliwa: ')
litr = int(strlitr)
print('Twoja fura spala '+ str(litr*100/km) +' litrów/100km')