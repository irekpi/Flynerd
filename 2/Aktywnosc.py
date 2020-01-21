waga = float(input('podaj wage'))
wzrost = float(input('podaj wzrost'))
wiek = float(input('podaj wiek'))
plec = input('podaj swoja plec "k" lub "M"')
s = 0
akty = 0

if plec == 'k' or plec == 'K':
    s = -161
if plec == 'M' or plec == 'm':
    s = 5

PMM = int(10*waga + 6.25*wzrost - 5*wiek + s)

print('PMM', PMM)

aktywnosc = int(input('wybierz \n1 len duzy, \n2 - mniejszy len, \n3 - troche aktywny, \n4 - aktywny'))
if aktywnosc == 1:
    akty = 1.0
if aktywnosc == 2:
    akty = 2.0
if aktywnosc == 3:
    akty = 3.0
if aktywnosc == 4:
    akty = 4.0
if aktywnosc == 5:
    akty = 5.0
ostatecznie = PMM*akty
print ('ostatecznie twoje zapotrzebowanie to sciema i nie jedz czipsow grubasie', '\n', ostatecznie)
