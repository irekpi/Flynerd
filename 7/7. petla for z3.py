names = str(input('podaj liste imion'))

names.replace(',', '')
for name in names.split(): 
    print('czesc', name.replace(',', ''))
