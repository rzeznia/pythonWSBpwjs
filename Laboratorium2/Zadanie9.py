alfabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for litera in alfabet:
    for x in range(0, 2):
        if x % 2 == 0:
            print(litera.upper(), end='')
        else:
            print(litera, end='')
print()
for litera in alfabet:
    for x in range(0, 2):
        if x % 2 == 0:
            print(litera, end='')
        else:
            print(litera.upper(), end='')