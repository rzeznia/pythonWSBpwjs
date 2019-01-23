# 1. Napisz program, który pyta o wiek i w zależności od podanej wartości, mówi czy ktoś jest pełnoletni czy nie.
# 2. Rozbuduj program 1 tak, by podawał:
# •Dla osoby pełnoletniej od ilu lat jest pełnoletnia
# •Dla osoby niepełnoletniej –ile lat brakuje jej jeszcze do pełnoletniości

strwiek = input("Podaj wiek")
wiek = int(strwiek)
if(wiek >= 18):
    print('Pelnoletni od '+ str(wiek-18) + ' lat.')
else:
    print('Niepełnoletni! Pełnoletnosć za ' + str(18-wiek) + ' lat')