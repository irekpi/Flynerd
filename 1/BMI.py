print('robimy zapotrzebowanie kaloryczne')
masa = float(input('podaj mase w kg'))
wzrost = float(input('podaj wzrost w cm'))
wiek = float(input('podaj wiek'))
s = str(input('jestes kobieta czy mezczyzna? podaj k lub m'))


if s == 'k':
    p = 10 * masa + 6.25 * wzrost - 5 * wiek - 161
    print(p)
if s == 'm':
    p = 10 * masa + 6.25 * wzrost - 5 * wiek +5
    print(p)

x = str(input('teraz w zaleznosci od tego czy jestes tluscioszkiem wybierz aktywnosc: 1, 2, 3'))

if x == '1':
    print(p*1)
if x == '2':
    print(p*2)
if x == '3':
    print(p*3)
