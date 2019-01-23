#BMI

strwaga = input("Podaj wagę ciała: ")
waga = int(strwaga)
strcenty = input('Podaj wzrost w cm: ')
metry = int(strcenty) / 100

BMI = waga / (metry*metry)
print('BMI: ' + str(BMI))

if(BMI < 18.5):
    print('Niedowaga')
elif(BMI < 24.9):
    print('Waga w normie')
elif(BMI < 29.9):
    print('Nadwaga')
else:
    print("Otyłość")
