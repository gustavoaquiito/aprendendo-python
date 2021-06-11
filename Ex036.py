casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'para pagar uma casa de {casa:.2f} em {anos} anos', end=''   )
print(f'a prestação será de {prestação:.2f}')
if prestação <= minimo:
    print('Emprétimo pode ser CONCEDIDO!')
else:
    print('Emprétimo NEGADO!')
 