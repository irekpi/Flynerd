age = int(input('ile masz lat?'))
zostalo = 18 - age

if age >= 18 and age < 100:
    print('dorosly')
elif age >= 100:
    print('w takim razie 200!')
else:
    print('podrosnij jeszcze: {} i bedziesz pelnoletni' .format(zostalo))

BMI= float(input(' podaj swoje BMI w przedziale od 0 do 100'))

if BMI < 18.5:
    print(' niedowaga')
if BMI >= 18.5 and BMI < 24:
    print (' waga normalna')
if BMI>= 24 and BMI < 26.5:
    print (' lekka nadwaga')
if BMI >= 26.5 and BMI <30:
    print ('nadwaga')
if BMI >= 30 and BMI <35:
    print ('1 st otylosci')
if BMI >= 35 and BMI <40:
    print ('2 st otylosci')
if BMI >= 40:
    print ('3 st otylosci - za gruby')
