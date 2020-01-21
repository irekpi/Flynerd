print ('podaj trzy dowolne liczby')
jeden = float(input ('podaj pierwsza'))
dwa = float(input ('podaj druga'))
trzy = float (input (' podaj trzecia'))

if (jeden > dwa and dwa > trzy):
    print (jeden, dwa, trzy)
elif (jeden < dwa and jeden > trzy):
    print (dwa, jeden, trzy)
elif (jeden < trzy and dwa > jeden):
    print (trzy, dwa, jeden)
elif (dwa > jeden and trzy > dwa):
    print('trzy, jeden, dwa')

if ( jeden > dwa and jeden > trzy):
    maximum = jeden
elif (dwa > jeden and dwa > trzy):
    maximum = dwa
else:
    maximum = trzy
print (maximum)
