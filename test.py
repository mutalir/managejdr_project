from pnj.pnj import Pnj

Paysan = Pnj('Paysan')
Paysan.Equiper()
caracs = Paysan.AfficherCaracs()

for key, value in caracs.items():
    if type(value) != dict:
        print(f'{f"{key}":<13}{"  -->  "}{f"{value}":<10}')
    else:
        print(f'{key + " :":<13}')
        for key2, value2 in value.items():
            print()
            print(f'{key2 + " :":>20}')
            for key3, value3 in value2.caracs.items():
                print(f'{f"{key3}":>20}{"  -->  "}{f"{value3}":<10}')
