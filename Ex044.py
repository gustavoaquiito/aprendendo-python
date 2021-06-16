print('{:=^40}'.format('LOJAS AQUIITO'))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela} SEM JUROS')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc =  int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de {parcela:.2f} COM JUROS')
else:
    total = preço
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print(f'sua compra de {preço:.2f} vai custar {total:.2f} no final.')
