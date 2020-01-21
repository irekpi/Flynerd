imie = input('podaj imiona ciagiem')

for i in imie.split():
    print('czesc', i.replace(',', ''))
