sentence = 'Kurs Pythona jest prosty i przyjemny.'

print(len(sentence))
print(sentence.find('p'), sentence.find(' ', 18), '\n', sentence[18:24])
print(sentence[7])
print(sentence[12])
print(sentence[-4])

sentence = sentence.replace('u', 'ż')
sentence = sentence.replace('o', 'u')
print(sentence)


imie = input('podaj imie')
nazwisko = input('podaj nazwisko')
tel = input('podaj tel')

print('imie ma tylko cyfry', imie.isalnum())
print('nazwisko ma tylko cyfry', nazwisko.isalnum())
print('numer ma tylko liczby', tel.isdigit())

print('Twoje imie to ', imie.capitalize())
print('Twoje nazwisko to ', nazwisko.capitalize())
print('twoj tel to', tel.replace('-', ' '))

personel = imie + ' ' + nazwisko + ' ' + tel
print(imie + ' ' + nazwisko + ' ' + tel)
print(len(personel))
