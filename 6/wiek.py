wiek = int(input('podaj swoj wiek'))

if wiek >= 18 and wiek < 100:
    print('gratulacje masz wiecej niz 18 lat')
if wiek >= 100:
    print('200! i wiecej')
if wiek < 18:
    print('zostalo ci niestety ', 18 - wiek, 'do 18')

