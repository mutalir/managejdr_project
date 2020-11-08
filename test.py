from pnj.pnj import Pnj

Paysan = Pnj('Paysan')
Paysan.Equip()
caracs = Paysan.DisplayCaracs()

for key, value in caracs.items():
    print(key, '  -->  ', value)
