peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você esta abaixo do peso')
elif imc < 25:
    print('Você esta com o peso ideal')
elif imc < 30:
    print('Você esta com sobrepeso')
elif imc < 40:
    print('Você esta com obesidade')
else:
    print('Você esta com Obesidade mórbida')
