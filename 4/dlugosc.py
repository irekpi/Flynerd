szer = 42
print('-' * szer)
print(' |  czas  |  Zawodnik  |  data  |')
print('>' * szer)
print('|  {:6.3f}  |  {:10s}  |  {:10s}  |' .format(9.56, 'bolt', '11.1.11'))
print('|  {:6.3f}  |  {:10s}  |  {:10s}  |' .format(9.56, 'bolt', '11.1.11'))
print('|  {:6.3f}  |  {:10s}  |  {:10s}  |' .format(9.56, 'bolt', '11.1.11'))
print('>' * szer)


waluta = "dolar"
us = 1
pln = 4.08234915
print("Aktualnie {}d {}s kosztuje {:.2f} zł" .format(us, waluta, pln))

dl = float(input('podaj dl w cm '))
metr = float(dl*0.01)
cal = dl*2
print('dlugosc w metrach to: {:.4f} \n dl w calach to: {:.4f}' .format(metr, cal))
