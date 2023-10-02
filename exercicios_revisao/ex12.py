eleitores = int(input('Número total de eleitores: '))
votosBrancos = int(input('Número de votos brancos: '))
votosNulos = float(input('Número de votos nulos: '))
votosValidos = int(input('Número de votos válidos: '))



print(f'Número total de eleitores: {eleitores}')
print('Porcentagem de votos brancos: {:.1f}%' .format((votosBrancos / eleitores) * 100))
print('Porcentagem de votos nulos: {:.1f}%' .format((votosNulos / eleitores) * 100))
print('Porcentagem de votos válidos: {:.1f}%' .format((votosValidos / eleitores) * 100))
