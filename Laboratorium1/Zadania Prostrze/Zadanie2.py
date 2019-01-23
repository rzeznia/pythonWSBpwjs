#sprawdzenie parzystosci

strval = input('Podaj lcizbe do sprawdzenia parzysości: ')
val = int(strval)
if(val % 2 == 0):
    print('Liczba '+strval+ ' jest parzysta')
else:
    print('Liczba '+strval+ ' NIE jest parzysta')