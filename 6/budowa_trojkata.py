a = float(input('podaj a'))
b = float(input(' podaj b'))
c = float( input(' podaj c'))


if a > b:
    temp = b
    b = a
    a = temp
if a > c:
    temp = c
    c = a
    a = temp
if b > c:
    temp = c
    c = b
    b = temp

print(a, b, c)

trojkat = False

if a + b > c:
    trojkat = True
    print('da sie go zrobic')
else:
    print('niestety')
    

if trojkat and a**2 + b**2 == c**2:
    print('pitagoras')
    if a/3 == b/4 == c/5:
        print('aaa')
elif trojkat:
    print('nie pitagoras')

