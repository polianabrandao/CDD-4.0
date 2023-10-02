qtdmaca = int(input('Digite a quantidade de maçãs? '))

if qtdmaca < 12:
    preco = qtdmaca * 1.30
else:
    preco = qtdmaca
print(f'Total: R${preco}')