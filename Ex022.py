n = str(input('Digite o seu nome completo: ')).strip(' ')
print('Analisandoo seu nome...')
print(f'O seu nome em maiúsculas é {n.upper()}')
print(f'O seu nome em minúsculas é {n.lower()}')
print(f'Seu nome tem ao todo {len(n) - n.count(" ")} letras')
print(f'Seu primeiro nome tem {n.find(" ")} letras')
