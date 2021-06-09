a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if b > a and b > c:
    maior = b
if a > b and a > c:
    maior = a
if c > b and c > b:
    maior = c

print(f'O menor valor foi {menor}')
print(F'O maior valor foi {maior}')
