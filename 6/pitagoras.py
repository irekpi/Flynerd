a = float(input('podaj a'))
b = float(input(' podaj b'))
c = float(input(' podaj c'))

if a > b and a > c:
    print(' a najdluzsze')
    if b + c > a:
        print('mozna')
    else:
        print('nie')
if b > c and a > a:
    print(' b najdluzjsze')
    if a + c > b:
        print('mozna')
    else:
        print('nie mozna')
if c > a and c > b:
    print('c najdlzusze')
    if a + b > c:
        print('mozna')
    else:
        print('nie mozna')



