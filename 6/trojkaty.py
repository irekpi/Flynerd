x = float(input('podaj jeden bok'))
y = float(input(' podaj 2 bok'))
z = float(input(' podaj 3 bok'))

if x > y:
    temp = y
    y = x
    x = temp
if y > z:
    temp = z
    z = y
    y = temp
if x > z:
    temp = z
    z = x
    x = temp

print(x, y, z)

if x + y > z:
    print(' buduj smialo')
else:
    print (' nie da rady')
if x**2 + y**2 == z**2:
    print('jest pitagorejski')
    if x/3 == y/4 and y/4 == z/5:
        print('egipski')
    if x/3 != y/4 != z/5:
        print('nie jest ani jednym ani drugim')
if x**2 + y**2 != z**2:
    print('nie jest pitagorejski ')
