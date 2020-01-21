imiona = {'Adam': 'm',
           'Ewa': 'w',
           'Jan': 'm'}

imie = input('podaj imie')

if imie.endswith('a'):
    print('imie zenskie')
else:
    print('imie meskie')
if imie not in list(imiona.keys()):
    dodanie = input('nie ma cie w bazie, chcesz sie dodac? podaj t lub n')
    if dodanie == 't':
        plec = input(' jestes kobieta czy mezczyzna? podaj k lub m')
        if plec == 'm':
            imiona[imie] = str('m')
print(imiona.keys(), imiona.values())
