velocidade = float(input('Qual é a velocidadde atual do carro? '))
if velocidade > 80:
    print(f'MULTADO! Você exedeu o limite permitido que é de 80Km/H')
    multa = (velocidade-80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')