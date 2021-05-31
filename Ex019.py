import random
p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
lis = [p, s, t]
escolhido = random.choice(lis)
print(f'O aluno escolhido foi {escolhido}')