zbior = {'adam': 'men',
         'alex': 'men',
         'kasia': 'wom',
         'ola': 'wom'}

imie = input('podaj imie')


if imie in list(zbior.keys()):
    print(imie, zbior[imie])
else:
    print('podaj imie bo nie ma w bazie')
    gender = input('podaj m lub z')
    if gender == 'm':
        zbior[imie] = 'men'
    else:
        zbior[imie] = 'wom'
    print(list(zbior.keys()))
