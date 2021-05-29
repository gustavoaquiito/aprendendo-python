import math
co = float(input('Comprimento do cateto aposto: '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai midir {hi:.2f}')
