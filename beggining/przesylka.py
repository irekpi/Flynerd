weight = int(input('podaj wage przesylki'))
prem = str(input('podaj czy jesyt premium. T czy N?'))


def premium(prem):
  if prem == "T":
    print( 'cena za przesylke to  120')
  else:
    print(ground_shipping(weight))


def ground_shipping(weight):
  if weight <= 2:
    return weight*1.5+20
  elif weight > 2 and weight <=6:
    return weight*3 + 20
  elif weight > 6 and weight <= 10:
    return weight*4 + 20
  else:
    return weight*4.75 + 20


premium(prem)


