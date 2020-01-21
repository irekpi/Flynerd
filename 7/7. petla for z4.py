ilosc = int(input('podaj ile razy ma dzialac'))
          
for i in range(0, ilosc):
          liczba = int(input('podaj liczb'))
          if liczba % 3 == 0:
              print(' podzielna przez 3')
          if liczba % 4 == 0:
              print('liczba podzielna przez 4')
          if liczba % 4 == 0 and liczba % 3 == 0:
              print('hura')
          else:
              print('*')
          
    
