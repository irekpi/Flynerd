seriale = {'riverdale': 5,
           'casa': 3,
           'wisnie': 4,
           'marakuja': 5}
print('********')
print(list(seriale.keys()))
print(list(seriale.values()))
print('********')

nazwa = input('jaki serial chcesz zobaczyc?')

if nazwa in list(seriale.keys()):
    print(' to {} ma ocene {}' .format(nazwa, seriale[nazwa]))
else:
    dodanie = input('niestety nie ma go w bazie ale jesli chcesz to go dodamy powiedz tylko t lub n')
    if dodanie == 't':
        ocena = input('jaka jest jego ocena?')
        seriale[nazwa] = float(ocena)
    if dodanie == 'n':
        print('polecamy cos innego')
print('*********')
print(list(seriale.keys()))
print(list(seriale.values()))
